



   $(document).ready(function() {


        var value=new Array();
             var frm=0;
          var tll=3;


     $.ajax({
                type:'GET',
                url:"/get_tweets",
                success:function(data, textStatus, xhr) {
                    console.log(data);
                    var i = 0;
                    for (var prop in data['tweets'])
                    {
                        value[i++] = data['tweets'][prop];
                        if(i==1){
                            $("#bbbb1").append(prop);
                        }
                    }
                    //for (j= 0; j<value.length; j++)
                    //{
                        var j=0;
                        var z=2;
                        console.log(value[0]);
                    for(k=0; k<value[j].length; k++) {
                        if (k == 0 || k == 3) {
                            $("#bbbb" + z).append(value[j][k]['html']);
                            z++;
                            console.log(z)
                        }
                        else if (k > 4 && k < 8) {
                            $("#bbbb" + z).append(value[j][k]['html']);
                            console.log(z)
                        }
                    }
                    //console.log(value[0][0]['author_name']);


}
});
});


