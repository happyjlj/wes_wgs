# -*- coding: utf-8 -*-


import xlrd
from settings import MEDIA_ROOT
import re
import os


class ExcelImport:
	def __init__(self, file_name):
		# self.file_name = unicode(file_name, "utf-8")
		# 文件路径修改
		self.file_name = (MEDIA_ROOT + str(file_name)).replace("\\", "\/").decode("utf-8")
		print 'aaa:',file_name
		print 'bbb:',self.file_name
		self.workbook = xlrd.open_workbook(self.file_name)
		
		self.table = self.workbook.sheets()[0]
		# 获取总行数
		self.nrows = self.table.nrows
		# 获取总列数
		self.ncols = self.table.ncols

		self.cases = []
		# type_1 单列，排除空值，0值作图 type_2 qc_clean_n 双列 不需要排除0值，但是需要排除空值
		# type_3 双列 需要排除0值和空值	type_4 单列，取（）内的数值统计作图，排除空值，0值作图
		# type_5 单列，百分数，排除空值，0值作图	 5种类型 分别处理

		self.pattern = {
			"type_1": ["qc_clean", "qc_clean_reads",
						 "qc_clean_bases", "qc_adapter",
						 "qc_pool_lib_data", "qc_mapped",
						 "qc_paired",
						 "qc_insert", "qc_duplication",
						 "algin_clean_reads", "algin_reads_unique_target",
						 "algin_reads_unique_genome",
						 "algin_total_baseson_target",
						 "algin_total_basesnear_target",
						 "algin_total_seqon_target",
						 "algin_total_seqnear_target",
						 "algin_total_effective_yield", "algin_avg_seqdepthon_target",
						 "algin_avg_seqdepthnear_target",
						 "algin_avg_insert_size",
						 "algin_base_coveredon_target", "algin_base_coverednear_target",
						 "snp_total_snp", "snp_splicing_predicted",
						 "snp_utr3",
						 "snp_utr5",
						 "snp_utr5_utr3",
						 "snp_downstream",
						 "snp_exonic_splicing",
						 "snp_ncrna_exonic",
						 "snp_ncrna_exonic_splicing",
						 "snp_ncrna_intronic",
						 "snp_ncrna_splicing",
						 "snp_splicing",
						 "snp_stopgain",
						 "snp_stoploss",
						 "snp_unknown_info",
						 "snp_upstream",
						 "snp_upstream_downstream",
						 "snp_ti_tv",
						 "indel_total_indel",
						 "indel_utr3",
						 "indel_utr5",
						 "indel_utr5_utr3",
						 "indel_downstream",
						 "indel_exonic_splicing",
						 "indel_frameshift_insertion",
						 "indel_frameshift_deletion",
						 "indel_ncrna_exonic",
						 "indel_ncrna_exonic_splicing",
						 "indel_ncrna_intronic",
						 "indel_nonframeshift_deletion",
						 "indel_nonframeshift_insertion",
						 "indel_splicing",
						 "indel_stopgain",
						 "indel_stoploss",
						 "indel_unknown_info",
						 "indel_upstream",
						 "indel_upstream_downstream",
						 ],
			"type_2": ["qc_clean_n"],
			"type_3": ["qc_cleanq20",
						 "qc_cleanq30",
						 "qc_clean_gc",
						 "qc_raw_gc",
						 "qc_read_length", ],
			"type_4": ["algin_mapped_reads",
						 "algin_duplicate_reads",
						 "algin_unique_reads",
						 "snp_genome1000_and_dbsnp150",
						 "snp_genome1000_only",
						 "snp_dbsnp150_only",
						 "snp_novel",
						 "snp_het",
						 "snp_homo",
						 "snp_synonymous_snv",
						 "snp_nonsynonymous_snv",
						 "snp_exonic",
						 "snp_intergenic",
						 "snp_intronic",
						 "indel_genome1000_and_dbsnp150",
						 "indel_dbsnp150_only",
						 "indel_novel",
						 "indel_het",
						 "indel_homo",
						 "indel_exonic",
						 "indel_intergenic",
						 "indel_intronic",

						 ],
			"type_5": ["algin_feb_on_target",
						 "algin_feb_onnear_target",
						 "algin_fraction_unique_target", "algin_coverage_target_region",
						 "algin_coverage_near_target",
						 "algin_mismatch_in_target",
						 "algin_mismatch_in_total",
						 "algin_fraction_coveredt_4x",
						 "algin_fraction_covered_10x",
						 "algin_fraction_covered_20x",
						 "algin_fraction_covered_50x",
						 ]

		}
		self.cols = []

	
	def get_cases(self):
		res = []
		# 第一行列名字
		firstrow = self.table.row_values(0)
		
		for val in range(0, self.ncols):
			self.cols.append(firstrow[val])

		# 遍历所有列
		for x in range(0, self.ncols):
			if self.cols[x] in self.pattern["type_1"]:
				# 遍历所有行
				subcols = []
				bus_code = []
				for r in range(1, self.nrows):
					row = self.table.row_values(r)
					data = row[x];
					# 排除空值和零值
					if data == 0.0 or data == '':
						continue
					else:
						subcols.append(data)
						bus_code.append(row[0])

				res.append({
					"bus_code": bus_code,
					"name": self.cols[x],
					"list": subcols
				})

			elif self.cols[x] in self.pattern["type_2"]:
				subcols_1 = []
				subcols_2 = []
				bus_code=[]
				for r in range(1, self.nrows):
					row = self.table.row_values(r)
					data = row[x];
					# 排除空值
					if data == '':
						continue
					else:
						temdata = data.split(";")
						subcols_1.append(temdata[0])
						subcols_2.append(temdata[1])
						bus_code.append(row[0])

				res.append({
					"bus_code":bus_code,
					"name": self.cols[x] + '_1',
					"list": subcols_1
				})
				res.append({
					"bus_code": bus_code,
					"name": self.cols[x] + '_2',
					"list": subcols_2
				})

			elif self.cols[x] in self.pattern["type_3"]:
				subcols_1 = []
				subcols_2 = []
				bus_code = []
				for r in range(1, self.nrows):
					row = self.table.row_values(r)
					data = row[x];
					# 排除空值和零值
					if data == '' or data == 0.0 or data == "0.00;0.00":
						continue
					else:
						temdata = data.split(";")
						subcols_1.append(temdata[0])
						subcols_2.append(temdata[1])
						bus_code.append(row[0])

				res.append({
					"bus_code": bus_code,
					"name": self.cols[x] + '_1',
					"list": subcols_1
				})
				res.append({
					"bus_code": bus_code,
					"name": self.cols[x] + '_2',
					"list": subcols_2
				})

			elif self.cols[x] in self.pattern["type_4"]:
				# 遍历所有行
				subcols = []
				bus_code = []
				for r in range(1, self.nrows):
					row = self.table.row_values(r)
					if row[x] == '' or row[x] == 0.0:
						continue
					tem = row[x]
					try:
						data = re.findall(r'[(](.*?)%[)]', row[x]);
					except TypeError as e:
						print e
					# 排除空值和零值
					if data and len(data) == 1:
						if data[0] == 0.0 or data[0] == '':
							continue
						else:
							subcols.append(data)
							bus_code.append(row[0])
				res.append({
					"bus_code": bus_code,
					"name": self.cols[x],
					"list": subcols,
					'type': "percent"
				})
			elif self.cols[x] in self.pattern["type_5"]:
				# 遍历所有行
				subcols = []
				bus_code = []
				for r in range(1, self.nrows):
					row = self.table.row_values(r)
					data = row[x]
					# 排除空值和零值
					if data == 0.0 or data == '':
						continue
					else:
						subcols.append(data)
						bus_code.append(row[0])

				res.append({
					"bus_code": bus_code,
					"name": self.cols[x],
					"list": subcols,
					'type': "percent"
				})
		#del_files(self.file_name)
		return res
	###作图完成后删除服务器的文件
	def del_files(self):
		path=self.file_name
		print 'pp:',path
		os.remove(path)	
