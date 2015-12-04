



   $(document).ready(function() {


        var value=new Array();
             var frm=0;
          var tll=3;


     $.ajax({
                type:'GET',
                url:"/recommended_news",
                success:function(data, textStatus, xhr) {
                    console.log(data);
                    var i = 0;
                    for (var prop in data['news'])
                    {
                        value[i++] = data['news'][prop];
                        //console.log(value[0]);
                    }

                    for (j= 0; j<value.length; j++)
                    {
                        //var z=1;
                        console.log(value[0]);
                    for(k=1; k<value[j].length; k++)
                    {

                            $(".content" + k + " " + "h1").text(value[j][k-1]['title']);
                            $(".content" + k + " " + "h2").text(value[j][k-1]['category']);
                            $(".content" + k + " " + "img").attr('src',value[j][k-1]['image']);
                            $(".content" + k + " " + ".b1").attr('href','/tagnews/'+value[j][k-1]['category']);
                            $("#a" + k).attr('href','/fullnews/'+value[j][k-1]['category']);
                        console.log(value[j][k-1]['title'])
                    }
                    }



}
});
});


/**
 * Created by sony on 04-12-2015.
 */
