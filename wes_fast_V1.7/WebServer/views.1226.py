# coding:utf-8
import urllib
import urllib2
import json
import re
import os
import sys
import random
import math
import time
import csv
from django import forms
from django.contrib import admin, messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from django.db.models import Q
from mongoengine.queryset.visitor import Q
from django.template.response import TemplateResponse
from . import models
import time
from mongoengine import *
from bson.objectid import ObjectId
from datetime import date,datetime,timedelta

# 连接数据库
connect('wes_wgs', host='10.100.1.7', port=27017,username='wuser', password='berry2012')


#调用templates文件夹下面的home.html模板文件
#**************************************************
#***************	 主界面	*********************
#**************************************************

#**************************************************

def result(request):
	#print "strat:",time.strftime('%Y-%m-%d %H:%M:%S')	
	
	DB_data = models.Sample.objects(Q(bus_code__exact = 'xxdfgwergsd234asdf'))
	result_dict1 = None
	result_dict2 = None
	result_dict3 = None
	indexType = ''

	# 用于记录搜索值
	busCode = None
	isdisease1 = None
	isdisease2 = None
	isdisease3 = None
	disease_name = None
	age = None
	sam_type1 = None
	sam_type2 = None
	sex1 = None
	sex2 = None
	sex3 = None
	disease_phenotype = None
	probe1 = None
	probe2 = None
	probe3 = None
	probe4 = None
	probe5 = None
	ana_type1 = None
	ana_type2 = None
	ana_type3 = None
	ana_type4 = None
	ana_type5 = None

	Search_Flag = None

	if request.method == 'POST':
		Search_Flag = 1
		DB_data = models.Sample.objects.order_by('bus_code')
		if request.POST.has_key('busCode'):
			busCode = request.POST['busCode']
			if busCode:
				DB_data = DB_data(Q(bus_code__contains = busCode))
		if request.POST.has_key('age'):
			age = request.POST['age']
			if age:
				DB_data = DB_data(Q(age__contains = age))
		if request.POST.has_key('disease_name') and request.POST.has_key('disease_phenotype'):
			disease_name = request.POST['disease_name']
			disease_phenotype = request.POST['disease_phenotype']
			DB_data = DB_data(
				Q(body_check__contains = disease_name)
				| Q(body_check__contains = disease_phenotype))


		if request.POST.has_key('isdisease1'):
			isdisease1 = 'P'
		else:
			# 保证搜索不到即可
			isdisease1 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('isdisease2'):
			isdisease2 = 'N'
		else:
			# 保证搜索不到即可
			isdisease2 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('isdisease3'):
			isdisease3 = 'U'
		else:
			# 保证搜索不到即可
			isdisease3 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('isdisease1') or request.POST.has_key('isdisease2') or request.POST.has_key('isdisease3'):
			DB_data = DB_data(
				Q(is_ill__contains = isdisease1)
				| Q(is_ill__contains = isdisease2)
				| Q(is_ill__contains = isdisease3))


		if request.POST.has_key('sam_type1'):
			sam_type1 = '外周血'.decode('utf-8')
		else:
			# 保证搜索不到即可
			sam_type1 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('sam_type2'):
			sam_type2 = '脐带血'.decode('utf-8')
		else:
			# 保证搜索不到即可
			sam_type2 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('sam_type1') or request.POST.has_key('sam_type2'):
			DB_data = DB_data(
				Q(sample_type__contains = sam_type1)
				| Q(sample_type__contains = sam_type2))

		# models.Sample.objects.filter(bus_code__exact='7E6756').update(clinical_info=sam_type1)
		if request.POST.has_key('sex1'):
			sex1 = '男'.decode('utf-8')
		else:
			# 保证搜索不到即可
			sex1 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('sex2'):
			sex2 = '女'.decode('utf-8')
		else:
			# 保证搜索不到即可
			sex2 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('sex3'):
			sex3 = 'U'
		else:
			# 保证搜索不到即可
			sex3 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('sex1') or request.POST.has_key('sex2') or request.POST.has_key('sex3'):
			DB_data = DB_data(
				Q(sex__contains = sex1)
				| Q(sex__contains = sex2)
				| Q(sex__contains = sex3))


		if request.POST.has_key('probe1'):
			probe1 = 'WES_39M'
		else:
			# 保证搜索不到即可
			probe1 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('probe2'):
			probe2 = 'WES_50M'
		else:
			# 保证搜索不到即可
			probe2 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('probe3'):
			probe3 = 'WES_64M'
		else:
			# 保证搜索不到即可
			probe3 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('probe4'):
			probe4 = 'WGS'
		else:
			# 保证搜索不到即可
			probe4 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('probe5'):
			probe5 = 'Panel'
		else:
			# 保证搜索不到即可
			probe5 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if (request.POST.has_key('probe1') or
			request.POST.has_key('probe2') or
			request.POST.has_key('probe3') or
			request.POST.has_key('probe4') or
			request.POST.has_key('probe5')):
			DB_data = DB_data(
				Q(probe__contains = probe1)
				| Q(probe__contains = probe2)
				| Q(probe__contains = probe3)
				| Q(probe__contains = probe4)
				| Q(probe__contains = probe5))


		if request.POST.has_key('ana_type1'):
			ana_type1 = '外显子PLUS'.decode('utf-8')
		else:
			# 保证搜索不到即可
			ana_type1 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('ana_type2'):
			ana_type2 = '全外显子'.decode('utf-8')
		else:
			# 保证搜索不到即可
			ana_type2 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('ana_type3'):
			ana_type3 = '外显子CNV'.decode('utf-8')
		else:
			# 保证搜索不到即可
			ana_type3 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('ana_type4'):
			ana_type4 = '科技服务'.decode('utf-8')
		else:
			# 保证搜索不到即可
			ana_type4 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if request.POST.has_key('ana_type5'):
			ana_type5 = '新生儿位点筛查'.decode('utf-8')
		else:
			# 保证搜索不到即可
			ana_type5 = 'GHJDFTYHAERGVxsBXCGFNADERGZXFBGFSHNAEGF'
		if (request.POST.has_key('ana_type1') or
			request.POST.has_key('ana_type2') or
			request.POST.has_key('ana_type3') or
			request.POST.has_key('ana_type4') or
			request.POST.has_key('ana_type5')):
			DB_data = DB_data(
				Q(test_item__contains = ana_type1)
				| Q(test_item__contains = ana_type2)
				| Q(test_item__contains = ana_type3)
				| Q(test_item__contains = ana_type4)
				| Q(test_item__contains=ana_type5))
		#####增加时间项
		if request.POST.has_key('time_start'):
			startDate = request.POST['time_start']
			#start_date=time.strptime(startDate,"%Y-%m-%d")
			print 'S:',startDate
			#print start_date
		if request.POST.has_key('time_end'):
			endDate = request.POST['time_end']
			#end_date=time.strptime(endDate,"%Y-%m-%d")
			print 'E:',endDate
			#print end_date
		if request.POST.has_key('result_dict1_POST'):
			result_dict1 = 'result_dict1'
			indexType = 'qc'
			#DB_data = models.Sample.objects.order_by('bus_code')
		if request.POST.has_key('result_dict2_POST'):
			result_dict2 = 'result_dict2'
			indexType = 'algin'
		if request.POST.has_key('result_dict3_POST'):
			result_dict3 = 'result_dict3'
			indexType = 'snp_indel'
		###
		if startDate=='':
			s = "1970-01-01 00:00:00"
		else:
			s = startDate+" 00:00:00"
		if endDate=='':
			now=datetime.now()
			e=now.strftime("%Y-%m-%d %H:%M:%S")
		else:
			e = endDate+" 23:59:59"
		s_arr=time.strptime(s,'%Y-%m-%d %H:%M:%S')
		e_arr=time.strptime(e,'%Y-%m-%d %H:%M:%S')
		s_time=int(time.mktime(s_arr))
		e_time=int(time.mktime(e_arr))
		print 'sss:',s_time
		print 'eee:',e_time
		print type(DB_data)
		print 'C1:',DB_data.count()
		i=0
		for m in DB_data:
			oid=m.id
			a=ObjectId(oid)
			b=time.strftime("%Y-%m-%d %H:%M:%S",a.generation_time.timetuple())
			timeArray = time.strptime(b,'%Y-%m-%d %H:%M:%S')
			d_time = int(time.mktime(timeArray))
			if d_time >=s_time and d_time <=e_time:
				print 'aaa:',d_time,m.bus_code
				continue
			else:
				DB_data=DB_data.filter(id__contains=m.id)
		print "I:",i
		print 'C:',DB_data.count()
	response =  TemplateResponse(
		request,
	   # 'home.html',
		'result.html',
		{
			'ishome': True,
			'DB_data': DB_data,
			'result_dict1': result_dict1,
			'result_dict2': result_dict2,
			'result_dict3': result_dict3,
			'indexType':indexType,
			'count': str(DB_data.count()),

			'Search_Flag': Search_Flag,
			'busCode': busCode,
			'isdisease1': isdisease1,
			'isdisease2': isdisease2,
			'isdisease3': isdisease3,
			'disease_name': disease_name,
			'age': age,
			'sam_type1': sam_type1,
			'sam_type2': sam_type2,
			'sex1': sex1,
			'sex2': sex2,
			'sex3': sex3,
			'disease_phenotype': disease_phenotype,
			'probe1': probe1,
			'probe2': probe2,
			'probe3': probe3,
			'probe4': probe4,
			'probe5': probe5,
			'ana_type1': ana_type1,
			'ana_type2': ana_type2,
			'ana_type3': ana_type3,
			'ana_type4': ana_type4,
			'ana_type5': ana_type5,

		})
	return response
	

###两个数值的散点图
def cartgram(request):
	dataType_1 = ''
	dataList_1 = ''
	dataType_2 = ''
	dataList_2 = ''
	dataBus_Code = ''
	dataList_str = None
	if request.method == 'POST':
		# 检索结果总共有多少条数

		dataType = request.POST['dataType']
		DB_Data_All=models.Sample.objects.all()
		dataList1_cache = ''
		dataList2_cache = ''

		# 检索结果总共有多少条数
		CountNum = int(request.POST['Count'])
		dataBus_Code = ''
		CountChecked = 0
		# 通过BusCode获取该dataType列
		for m in range(0,CountNum):
			if request.POST.has_key('count' + str(m)):
				inputCheckBox_BusCode = request.POST['BusCode_value' + str(m)]
				DB_Data_Cache = DB_Data_All.filter(bus_code__exact=inputCheckBox_BusCode)
				if DB_Data_Cache:
					if dataType == 'cleanq20':
						dataType_1 = 'cleanq20_1'
						dataType_2 = 'cleanq20_2'
						dataList_str = DB_Data_Cache[0].qc[0].cleanq20
						if dataList_str=='.' or dataList_str=='' or dataList_str=='.;.' or dataList_str=='0;0':
							continue
					elif dataType == 'cleanq30':
						dataType_1 = 'cleanq30_1'
						dataType_2 = 'cleanq30_2'
						dataList_str = DB_Data_Cache[0].qc[0].cleanq30
						if dataList_str=='.' or dataList_str=='' or dataList_str=='.;.' or dataList_str=='0;0':
							continue
					elif dataType == 'clean_n':
						dataType_1 = 'clean_n_1'
						dataType_2 = 'clean_n_2'
						dataList_str = DB_Data_Cache[0].qc[0].clean_n
						if dataList_str=='.' or dataList_str=='' or dataList_str=='.;.' or dataList_str=='0;0':
							continue
					elif dataType == 'clean_gc':
						dataType_1 = 'clean_gc_1'
						dataType_2 = 'clean_gc_2'
						dataList_str = DB_Data_Cache[0].qc[0].clean_gc
						if dataList_str=='.' or dataList_str=='' or dataList_str=='.;.' or dataList_str=='0;0':
							continue
					elif dataType == 'raw_gc':
						dataType_1 = 'raw_gc_1'
						dataType_2 = 'raw_gc_2'
						dataList_str = DB_Data_Cache[0].qc[0].raw_gc
						if dataList_str=='.' or dataList_str=='' or dataList_str=='.;.' or dataList_str=='0;0':
							continue
					elif dataType == 'read_length':
						dataType_1 = 'read_length_1'
						dataType_2 = 'read_length_2'
						dataList_str = DB_Data_Cache[0].qc[0].read_length
						if dataList_str=='.' or dataList_str=='' or dataList_str=='.;.' or dataList_str=='0;0':
							continue
					if 	dataList_str:
						dataList_str_cache = dataList_str.split(';')
						dataList1_cache = dataList1_cache + str(dataList_str_cache[0]) + ';'
						dataList2_cache = dataList2_cache + str(dataList_str_cache[1]) + ';'
						dataBus_Code = dataBus_Code + str(inputCheckBox_BusCode) + ';'
						CountChecked = CountChecked + 1

		dataList_1 = dataList1_cache + '/count =' + str(CountChecked)
		dataList_2 = dataList2_cache + '/count =' + str(CountChecked)
		dataBus_Code = dataBus_Code + '/count =' + str(CountChecked)

	# DB_data = models.Sample.objects.order_by('bus_code')
	response =  TemplateResponse(
		request,
		'scattergram.html',
		{
			'type_1': dataType_1,	   # 修改
			'list_1': dataList_1,	   # 修改
			'type_2': dataType_2,	   # 修改
			'list_2': dataList_2,
			'dataBus_Code' : dataBus_Code,
		}
	)
	return response

##单个数值的散点图
def single(request):
	dataList = ''
	dataType = ''
	dataBus_Code = ''
	dataList_str = None
	if request.method == 'POST':
		# 检索结果总共有多少条数
		dataType = request.POST['dataType']
		DB_Data_All=models.Sample.objects.all()
		dataList_cache = ''
		# 检索结果总共有多少条数
		CountNum = int(request.POST['Count'])
		dataBus_Code = ''
		CountChecked = 0
		# 通过BusCode获取该dataType列
		for m in range(0,CountNum):
			if request.POST.has_key('count' + str(m)):
				inputCheckBox_BusCode = request.POST['BusCode_value' + str(m)]
				DB_Data_Cache = DB_Data_All.filter(bus_code__exact= inputCheckBox_BusCode)
				if DB_Data_Cache:
					# 全部的需要画Single的字段
					if dataType == 'qc_clean_per':
						dataList_str = DB_Data_Cache[0].qc[0].clean_per
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_clean_reads':
						dataList_str = DB_Data_Cache[0].qc[0].clean_reads
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_clean_bases':
						dataList_str = DB_Data_Cache[0].qc[0].clean_bases
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_adapter':
						dataList_str = DB_Data_Cache[0].qc[0].adapter
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_pool_lib_data':
						dataList_str = DB_Data_Cache[0].qc[0].pool_lib_data
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_mapped':
						dataList_str = DB_Data_Cache[0].qc[0].mapped
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_paired':
						dataList_str = DB_Data_Cache[0].qc[0].paired
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_insert':
						dataList_str = DB_Data_Cache[0].qc[0].insert
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'qc_duplication':
						dataList_str = DB_Data_Cache[0].qc[0].duplication
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_clean_reads':
						dataList_str = DB_Data_Cache[0].algin[0].clean_reads
						#print "1:",dataList_str
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
						#print dataList_str
					elif dataType == 'align_mapped_reads':
						tmp=DB_Data_Cache[0].algin[0].mapped_reads
						if tmp=="." or tmp=='' or tmp=='0(%)' or tmp=="0":
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].mapped_reads.split('(')[1].split('%)')[0])/100
					elif dataType == 'align_duplicate_reads':
						tmp=DB_Data_Cache[0].algin[0].duplicate_reads
						if tmp=="." or tmp=='' or tmp=='0(%)' or tmp=="0":
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].duplicate_reads.split('(')[1].split('%)')[0])/100
					elif dataType == 'align_unique_reads':
						tmp=DB_Data_Cache[0].algin[0].unique_reads
						if tmp=="." or tmp=='' or tmp=='0(%)' or tmp=="0":
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].unique_reads.split('(')[1].split('%)')[0])/100
					elif dataType == 'align_reads_unique_target':
						dataList_str = DB_Data_Cache[0].algin[0].reads_unique_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_reads_unique_genome':
						dataList_str = DB_Data_Cache[0].algin[0].reads_unique_genome
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_total_baseson_target':
						dataList_str = DB_Data_Cache[0].algin[0].total_baseson_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_total_basesnear_target':
						dataList_str = DB_Data_Cache[0].algin[0].total_basesnear_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_total_seqon_target':
						dataList_str = DB_Data_Cache[0].algin[0].total_seqon_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_total_seqnear_target':
						dataList_str = DB_Data_Cache[0].algin[0].total_seqnear_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_total_effective_yield':
						dataList_str = DB_Data_Cache[0].algin[0].total_effective_yield
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_feb_on_target':
						tmp=DB_Data_Cache[0].algin[0].feb_on_target
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].feb_on_target.split('%')[0])/100
					elif dataType == 'align_feb_onnear_target':
						tmp=DB_Data_Cache[0].algin[0].feb_onnear_target
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].feb_onnear_target.split('%')[0])/100
					elif dataType == 'align_fraction_unique_target':
						tmp=DB_Data_Cache[0].algin[0].fraction_unique_target
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].fraction_unique_target.split('%')[0])/100
					elif dataType == 'align_avg_seqdepthon_target':
						dataList_str = DB_Data_Cache[0].algin[0].avg_seqdepthon_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_avg_seqdepthnear_target':
						dataList_str = DB_Data_Cache[0].algin[0].avg_seqdepthnear_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_avg_insert_size':
						dataList_str = DB_Data_Cache[0].algin[0].avg_insert_size
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_base_coveredon_target':
						dataList_str = DB_Data_Cache[0].algin[0].base_coveredon_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_coverage_target_region':
						tmp=DB_Data_Cache[0].algin[0].coverage_target_region
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].coverage_target_region.split('%')[0])/100
					elif dataType == 'align_base_coverednear_target':
						dataList_str = DB_Data_Cache[0].algin[0].base_coverednear_target
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'align_coverage_near_target':
						tmp=DB_Data_Cache[0].algin[0].coverage_near_target
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].coverage_near_target.split('%')[0])/100
					elif dataType == 'align_mismatch_in_target':
						tmp=DB_Data_Cache[0].algin[0].mismatch_in_target
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].mismatch_in_target.split('%')[0])/100
					elif dataType == 'align_mismatch_in_total':
						tmp=DB_Data_Cache[0].algin[0].mismatch_in_total
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].mismatch_in_total.split('%')[0])/100
					elif dataType == 'align_fraction_covered_4x':
						dataList_str = float(DB_Data_Cache[0].algin[0].fraction_coveredt_4x.split('%')[0])/100
					elif dataType == 'align_fraction_covered_10x':
						tmp=DB_Data_Cache[0].algin[0].fraction_covered_10x
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].fraction_covered_10x.split('%')[0])/100
					elif dataType == 'align_fraction_covered_20x':
						tmp=DB_Data_Cache[0].algin[0].fraction_covered_20x
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].fraction_covered_20x.split('%')[0])/100
					elif dataType == 'align_fraction_covered_50x':
						tmp=DB_Data_Cache[0].algin[0].fraction_covered_50x
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].algin[0].fraction_covered_50x.split('%')[0])/100
					elif dataType == 'snp_total_snp':
						dataList_str = DB_Data_Cache[0].snp[0].total_snp
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_genome1000_and_dbsnp150':
						tmp=DB_Data_Cache[0].snp[0].genome1000_and_dbsnp150
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].genome1000_and_dbsnp150.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_genome1000_only':
						tmp=DB_Data_Cache[0].snp[0].genome1000_only
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%' :
							continue
						dataList_str = DB_Data_Cache[0].snp[0].genome1000_only.split('(')[1].split('%)')[0]
					elif dataType == 'snp_dbsnp150_only':
						tmp=DB_Data_Cache[0].snp[0].dbsnp150_only
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].dbsnp150_only.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_novel':
						tmp=DB_Data_Cache[0].snp[0].novel
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].novel.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_het':
						tmp=DB_Data_Cache[0].snp[0].het
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].het.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_homo':
						tmp=DB_Data_Cache[0].snp[0].homo
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].homo.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_synonymous_snv':
						tmp=DB_Data_Cache[0].snp[0].synonymous_snv
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].synonymous_snv.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_nonsynonymous_snv':
						tmp=DB_Data_Cache[0].snp[0].nonsynonymous_snv
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].nonsynonymous_snv.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_exonic':
						tmp=DB_Data_Cache[0].snp[0].exonic
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].exonic.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_intergenic':
						tmp=DB_Data_Cache[0].snp[0].intergenic
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].intergenic.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_intronic':
						tmp=DB_Data_Cache[0].snp[0].intronic
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].snp[0].intronic.split('(')[1].split('%)')[0])/100
					elif dataType == 'snp_splicing_predicted':
						dataList_str = DB_Data_Cache[0].snp[0].splicing_predicted
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_utr3':
						dataList_str = DB_Data_Cache[0].snp[0].utr3
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_utr5':
						dataList_str = DB_Data_Cache[0].snp[0].utr5
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_utr5_utr3':
						dataList_str = DB_Data_Cache[0].snp[0].utr5_utr3
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_downstream':
						dataList_str = DB_Data_Cache[0].snp[0].downstream
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_exonic_splicing':
						dataList_str = DB_Data_Cache[0].snp[0].exonic_splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_ncrna_exonic':
						dataList_str = DB_Data_Cache[0].snp[0].ncrna_exonic
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_ncrna_exonic_splicing':
						dataList_str = DB_Data_Cache[0].snp[0].ncrna_exonic_splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_ncrna_intronic':
						dataList_str = DB_Data_Cache[0].snp[0].ncrna_intronic
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_ncrna_splicing':
						dataList_str = DB_Data_Cache[0].snp[0].ncrna_splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_splicing':
						dataList_str = DB_Data_Cache[0].snp[0].splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_stopgain':
						dataList_str = DB_Data_Cache[0].snp[0].stopgain
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_stoploss':
						dataList_str = DB_Data_Cache[0].snp[0].stoploss
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_unknown_info':
						dataList_str = DB_Data_Cache[0].snp[0].unknown_info
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_upstream':
						dataList_str = DB_Data_Cache[0].snp[0].upstream
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_upstream_downstream':
						dataList_str = DB_Data_Cache[0].snp[0].upstream_downstream
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'snp_ti_tv':
						dataList_str = DB_Data_Cache[0].snp[0].ti_tv
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_total_indel':
						dataList_str = DB_Data_Cache[0].indel[0].total_indel
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_genome1000_and_dbsnp150':
						tmp=DB_Data_Cache[0].indel[0].genome1000_and_dbsnp150
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].genome1000_and_dbsnp150.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_dbsnp150_only':
						tmp=DB_Data_Cache[0].indel[0].dbsnp150_only
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].dbsnp150_only.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_novel':
						tmp=DB_Data_Cache[0].indel[0].novel
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].novel.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_het':
						tmp=DB_Data_Cache[0].indel[0].het
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].het.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_homo':
						tmp=DB_Data_Cache[0].indel[0].homo
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].homo.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_exonic':
						tmp=DB_Data_Cache[0].indel[0].exonic
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].exonic.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_intergenic':
						tmp=DB_Data_Cache[0].indel[0].intergenic
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].intergenic.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_intronic':
						tmp=DB_Data_Cache[0].indel[0].intronic
						if tmp=="." or tmp=='' or tmp=="0" or tmp=='0%':
							continue
						dataList_str = float(DB_Data_Cache[0].indel[0].intronic.split('(')[1].split('%)')[0])/100
					elif dataType == 'indel_utr3':
						dataList_str = DB_Data_Cache[0].indel[0].utr3
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_utr5':
						dataList_str = DB_Data_Cache[0].indel[0].utr5
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_utr5_utr3':
						dataList_str = DB_Data_Cache[0].indel[0].utr5_utr3
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_downstream':
						dataList_str = DB_Data_Cache[0].indel[0].downstream
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_exonic_splicing':
						dataList_str = DB_Data_Cache[0].indel[0].exonic_splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_frameshift_deletion':
						dataList_str = DB_Data_Cache[0].indel[0].frameshift_deletion
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_frameshift_insertion':
						dataList_str = DB_Data_Cache[0].indel[0].frameshift_insertion
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_ncrna_exonic':
						dataList_str = DB_Data_Cache[0].indel[0].ncrna_exonic
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_ncrna_exonic_splicing':
						dataList_str = DB_Data_Cache[0].indel[0].ncrna_exonic_splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_ncrna_intronic':
						dataList_str = DB_Data_Cache[0].indel[0].ncrna_intronic
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_nonframeshift_deletion':
						dataList_str = DB_Data_Cache[0].indel[0].nonframeshift_deletion
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_nonframeshift_insertion':
						dataList_str = DB_Data_Cache[0].indel[0].nonframeshift_insertion
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_splicing':
						dataList_str = DB_Data_Cache[0].indel[0].splicing
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_stopgain':
						dataList_str = DB_Data_Cache[0].indel[0].stopgain
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_stoploss':
						dataList_str = DB_Data_Cache[0].indel[0].stoploss
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_unknown_info':
						dataList_str = DB_Data_Cache[0].indel[0].unknown_info
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_upstream':
						dataList_str = DB_Data_Cache[0].indel[0].upstream
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue
					elif dataType == 'indel_upstream_downstream':
						dataList_str = DB_Data_Cache[0].indel[0].upstream_downstream
						if dataList_str=="." or dataList_str=='' or float(dataList_str)==0.0:
							continue



					if dataList_str:
						dataList_cache = dataList_cache + str(dataList_str) + ';'
						dataBus_Code = dataBus_Code + str(inputCheckBox_BusCode) + ';'
						CountChecked = CountChecked + 1



		dataList = dataList_cache + '/count =' + str(CountChecked)
		dataBus_Code = dataBus_Code + '/count =' + str(CountChecked)

	response =  TemplateResponse(
		request,
		'singlescatergram.html',
		{
			'type': dataType,
			'list': dataList,
			'dataBus_Code' : dataBus_Code,
		}
	)
	return response



