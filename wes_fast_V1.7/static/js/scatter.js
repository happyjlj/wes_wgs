 <script type="text/javascript">
		var dom = document.getElementById("container");
		var myChart = echarts.init(dom);
		var app = {};
		var url=window.document.URL;
		s=url.split("=")[2].split(";");
		alert(s)
		test=[];
		num=2;
		var Arr = new Array(s.length);
    	for(var i = 0; i<Arr.length;i++){
   			 Arr[i] = new Array();
    		for(var j = 0;j<num;j++){
   		 		Arr[i][0] = i;
				Arr[i][1]=s[i];
   			 }
    	}
		option = null;
		option = {
			xAxis: {
				scale: true
			},
			yAxis: {
				scale: true
			},
			series: [{
				type: 'effectScatter',
				symbolSize: 20,
				data: [
					[172.7, 105.2],
					[153.4, 42]
				]
			}, {
				type: 'scatter',
				data:Arr,
			}]
		};
		;
		if (option && typeof option === "object") {
			myChart.setOption(option, true);
		}
       </script>