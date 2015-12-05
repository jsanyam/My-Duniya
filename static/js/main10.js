$(document).ready(function() {
	var value=new Array();
    var frm=0;
    var tll=3;
    var x=1;

	$.ajax({
		type:'GET',
        url:"/get_tweets",
        success:function(data, textStatus, xhr) {
			console.log(data);
			var i = 0;
			for (var prop in data['tweets']){
				value[i++] = data['tweets'][prop];
				if(i==x){
					$("#bbb1").html(prop+"("+x+")");
				}
			}    
						//for (j= 0; j<value.length; j++)
						//{
			var j=0;
			var z=2;
			console.log(value[0]);
			for(k=0; k<value[j].length; k++) {
				if (k == 0 || k == 3) {
					$("#bbbb" + z).html(value[x][k]['html']);
					z++;
					console.log(z)
				}
				else if (k > 4 && k < 8) {
					$("#bbbb" + z).html(value[x][k]['html']);
					console.log(z)
				}
			}
		}//console.log(value[0][0]['author_name']);
	});
	$("#xz").click(function(){
		if(x==1){
			$("#bbb1").html(x);
		    $.ajax({
			type:'GET',
			url:"/get_tweets",
			success:function(data, textStatus, xhr) {
				console.log(data);
				var i = 0;
				for (var prop in data['tweets']){
					value[i++] = data['tweets'][prop];
					if(i==x){
						$("#bbb1").html(prop+"("+i+")");
					}
				}
							//for (j= 0; j<value.length; j++)
							//{
				var j=0;
				var z=2;
				console.log(value[0]);
				for(k=0; k<value[x].length; k++) {
					if (k == 0 || k == 3) {
						$("#bbbb" + z).html(value[x][k]['html']);
						z++;
						console.log(z)
					}
					else if (k > 4 && k < 8) {
						$("#bbbb" + z).html(value[x][k]['html']);
						console.log(z)
					}
				}
			}//console.log(value[0][0]['author_name']);
		});
			x=5;
        }
		else{
			$("#bbb1").html(x);
		    $.ajax({
			type:'GET',
			url:"/get_tweets",
			success:function(data, textStatus, xhr) {
				console.log(data);
				var i = 0;
				for (var prop in data['tweets']){
					value[i++] = data['tweets'][prop];
					if(i==x){
						$("#bbb1").html(prop+"("+i+")");
					}
				}
							//for (j= 0; j<value.length; j++)
							//{
				var j=0;
				var z=2;
				console.log(value[0]);
				for(k=0; k<value[x].length; k++) {
					if (k == 0 || k == 3) {
						$("#bbbb" + z).html(value[x][k]['html']);
						z++;
						console.log(z)
					}
					else if (k > 4 && k < 8) {
						$("#bbbb" + z).html(value[x][k]['html']);
						console.log(z)
					}
				}
			}//console.log(value[0][0]['author_name']);
		});
			x--;
        }

	});
	$("#xz").click(function(){
		if(x==5){
			$("#bbb1").html(x);
		    $.ajax({
			type:'GET',
			url:"/get_tweets",
			success:function(data, textStatus, xhr) {
				console.log(data);
				var i = 0;
				for (var prop in data['tweets']){
					value[i++] = data['tweets'][prop];
					if(i==x){
						$("#bbb1").html(prop+"("+i+")");
					}
				}
							//for (j= 0; j<value.length; j++)
							//{
				var j=0;
				var z=2;
                var k;
				console.log(value[0]);
				for(k=0; k<value[x].length; k++) {
					if (k == 0 || k == 3) {
						$("#bbbb" + z).html(value[x][k]['html']);
						z++;
						console.log(z)
					}
					else if (k > 4 && k < 8) {
						$("#bbbb" + z).html(value[x][k]['html']);
						console.log(z)
					}
				}
			}//console.log(value[0][0]['author_name']);
		});
			x=1;
        }
		else{
			$("#bbb1").html(x);
		    $.ajax({
			type:'GET',
			url:"/get_tweets",
			success:function(data, textStatus, xhr) {
				console.log(data);
				var i = 0;
				for (var prop in data['tweets']){
					value[i++] = data['tweets'][prop];
					if(i==x){
						$("#bbb1").html(prop+"("+i+")");
					}
				}
							//for (j= 0; j<value.length; j++)
							//{
				var j=0;
				var z=2;
				console.log(value[0]);
				for(k=0; k<value[x].length; k++) {
					if (k == 0 || k == 3) {
						$("#bbbb" + z).html(value[x][k]['html']);
						z++;
						console.log(z)
					}
					else if (k > 4 && k < 8) {
						$("#bbbb" + z).html(value[x][k]['html']);
						console.log(z)
					}
				}
			}//console.log(value[0][0]['author_name']);
		});
			x++;
        }

	});
});


