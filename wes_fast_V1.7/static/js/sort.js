<!--关于 排序 的地方-->
<script type="text/javascript">
(function($){
    //插件
    $.extend($,{
        //命名空间
        sortTable:{
            sort: function (tableId, Idx) {
                //获取table
				
                var table = document.getElementById(tableId);
                // 获取第一个body
                var tbody = table.tBodies[0];
                //获取行数
                var tr = tbody.rows;
                //定义新的行数组
                var trValue = new Array();
                for (var i=0; i<tr.length; i++ ) {
                    trValue[i] = tr[i];  //将表格中各行的信息存储在新建的数组中
                }
				//alert(Idx)
                if (tbody.sortCol == Idx) {
                    trValue.reverse(); //如果该列已经进行排序过了，则直接对其反序排列,仅仅是反向排序。
                } else {
                    //trValue.sort(compareTrs(Idx));  //进行排序
					//数值列排序,注意被div封装之后要截取出数值，且检索结果中封装不能换行，否则会出现方框乱码
					//数值列排序,注意被div封装之后要截取出数值，且检索结果中封装不能换行，否则会出现方框乱码
					//数值列排序,注意被div封装之后要截取出数值，且检索结果中封装不能换行，否则会出现方框乱码
						
					if(Idx>=15 && Idx<18){
						//数值列排序,注意被div封装之后要截取出数值，且检索结果中封装不能换行，否则会出现方框乱码
						trValue.sort(function(tr1, tr2){
							var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
							var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						//	alert(value1+";"+value2)
							return (value1> value2) ? 1 : -1;
						});
					}else if(Idx>=18&&Idx<24){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split(';')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split(';')[0]);
						//alert(value1+";"+value2)
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=24 && Idx<32){
						trValue.sort(function(tr1, tr2){
							var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
							var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
							return (value1> value2) ? 1 : -1;
						});
					}else if(Idx>=32&&Idx<35){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('(')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('(')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=35 && Idx<42){
						trValue.sort(function(tr1, tr2){
							var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
							var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
							return (value1> value2) ? 1 : -1;
						});
					}else if(Idx>=42&&Idx<45){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('%')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('%')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=45&&Idx<49){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx==49){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('%')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('%')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx==50){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=51 && Idx<58){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('%')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('%')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx==58){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						//alert(value1+";"+alert(value2))
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=59 && Idx<70){
						trValue.sort(function(tr1, tr2){
						//alert(tr1.cells[Idx].innerHTML)
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('(')[1].split('%')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('(')[1].split('%')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=70 && Idx<88){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=88 && Idx<96){
						trValue.sort(function(tr1, tr2){
						//alert(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0])
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('(')[1].split('%')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0].split('(')[1].split('%')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else if(Idx>=96 && Idx<114){
						trValue.sort(function(tr1, tr2){
						var value1 = Number(tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						var value2 = Number(tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0]);
						return (value1> value2) ? 1 : -1;
							});
					}else{	
							trValue.sort(function(tr1, tr2){
							var value1 = tr1.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0];
							var value2 = tr2.cells[Idx].innerHTML.split('pointer;">')[1].split('</')[0];
							//alert(value1+";"+value2)
							return value1.localeCompare(value2);
						});
					}
                   /** trValue.sort(function(tr1, tr2){
                        var value1 = tr1.cells[Idx].innerHTML;
                        var value2 = tr2.cells[Idx].innerHTML;
                        return value1.localeCompare(value2);
                    });**/
                }
        
                var fragment = document.createDocumentFragment();  //新建一个代码片段，用于保存排序后的结果
                for (var i=0; i<trValue.length; i++ ) {
                    fragment.appendChild(trValue[i]);
                }
        
                tbody.appendChild(fragment); //将排序的结果替换掉之前的值
                tbody.sortCol = Idx;
            }
        }
    });          
})(jQuery);

function desc_change(id, str) {
    $("#desc_1").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"样本编号"+'</div>');
       
    $("#desc_2").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"产品类型"+'</div>');
    $("#desc_3").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"样本类型"+'</div>');
    $("#desc_4").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"性别"+'</div>');
    $("#desc_5").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"年龄"+'</div>');
	
	
    $("#desc_15").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"排序"+'</div>');
    $("#desc_16").html('<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+"排序"+'</div>');
    $("#" + id).html(str);
}
/*function desc_change(id, str) {
    $("#desc_1").html("样本编号");
    $("#desc_2").html("产品类型");
    $("#desc_3").html("样本类型");
    $("#desc_4").html("性别");
    $("#desc_5").html("年龄");

    $("#desc_15").html("排序");
    $("#desc_16").html("排序");
	//alert(id)
    $("#" + id).html(str);
}*/

function desc(id, str) {
    var htmlstr = $("#" + id).text().trim();
    var c = str;
    if (htmlstr == str) {
        c = str + '▼';
		//alert(c)
		s = '<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor: pointer;\'>'+str +'▼'+'</div>'
        $("#" + id).html(s);
    } else if (htmlstr == str + '▼') {
        c = str + '▲'
		s = '<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor:pointer;\'>'+str +'▲'+'</div>'
        $("#" + id).html(s);
    } else if (htmlstr == str + '▲') {
        c = str + '▼'
		s = '<div style=\'width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;cursor:pointer;\'>'+str +'▼'+'</div>'
        $("#" + id).html(s);
		
    }
    desc_change(id, s)
    }

</script>