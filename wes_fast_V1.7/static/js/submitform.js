    function SubmitForm(val1) {
        //原本需要提交的参数
        var dataType = val1;
        //创建url
        var url = "/single/";
        //创建form
        var form = $("<form></form>");
        //设置属性
        form.attr("action", url);
        form.attr("method", "post");
        //获取总数
        var Count = document.getElementById("Count").value;
        var i = 0;
        for (i = 0;i < (Count*1);i++) {
            var CountNow = 'count' + String(i);
            var ValueNow = 'value' + String(i);
            if (document.getElementById(CountNow).checked)
            {
			 datastate = true;
			 CheckValue_busCode = document.getElementById(CountNow).value;
			 }
            else {
             datastate = false;
			 CheckValue_busCode = ''
            }
            var inputCheckBox = $("<input type='checkbox' name=" + CountNow + ">");
			inputCheckBox.attr("checked", datastate);
			var inputCheckBox_BusCode = $("<input type='text' name=BusCode_" + ValueNow + ">");
            inputCheckBox_BusCode.attr("value", CheckValue_busCode);
            form.append(inputCheckBox);
			form.append(inputCheckBox_BusCode);
        }
        //需要后台传递
		var inputdataType = $("<input type='text' name='dataType'/>");
        inputdataType.attr("value", dataType);
        var inputCount = $("<input type='text' name='Count'/>");
        inputCount.attr("value", Count);
        form.append(inputdataType);
        form.append(inputCount);
        form.appendTo("body");
        form.hide();
        //提交表单
        form.submit();
    }
    function SubmitForm_2(val1) {
        //原本需要提交的参数
        var dataType = val1;
        //创建url
        var url = "/cartgram/";
        //创建form
        var form = $("<form></form>");
        //设置属性
        form.attr("action", url);
        form.attr("method", "post");
        //获取总数
        var Count = document.getElementById("Count").value;
        var i = 0;
        for (i = 0; i < (Count * 1); i++) {
            var CountNow = 'count' + String(i);
            var ValueNow = 'value' + String(i);
            if (document.getElementById(CountNow).checked) {
                datastate = true;
                CheckValue_busCode = document.getElementById(CountNow).value;
            }
            else {
                datastate = false;
                CheckValue_busCode = ''
            }
            var inputCheckBox = $("<input type='checkbox' name=" + CountNow + ">");
            inputCheckBox.attr("checked", datastate);
            var inputCheckBox_BusCode = $("<input type='text' name=BusCode_" + ValueNow + ">");
            inputCheckBox_BusCode.attr("value", CheckValue_busCode);
            form.append(inputCheckBox);
            form.append(inputCheckBox_BusCode);
        }
        //需要后台传递
        var inputdataType = $("<input type='text' name='dataType'/>");
        inputdataType.attr("value", dataType);
        var inputCount = $("<input type='text' name='Count'/>");
        inputCount.attr("value", Count);
        form.append(inputdataType);
        form.append(inputCount);
        form.appendTo("body");
        form.hide();
        //提交表单
        form.submit();
    }
