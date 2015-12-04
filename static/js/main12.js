



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
                            $("#a" + k).attr('href','/fullnews/'+value[j][k-1]['id']);
                        console.log(value[j][k-1]['title'])
                    }
                    }



}
});
var storeArraynews=new Array();
var ipp=0;
            console.log(ipp)
            type:'GET',
                url:"/recommended_news",
                success:function(data, textStatus, xhr) {
                    console.log(data);
                    var i = 0;
                    for (var prop in data['news'])
                    {
                        storeArraynews[i++] = data['news'][prop];
                        //console.log(value[0]);
                    }
                    console.log(storeArraynews[1][5])
                     var x = storeArraynews[1][5];
                     var x = x.split("-").join(" ");
                     $("#heading").append("<div>" + x + "</div>");

                    //console.log("pahuche")

                    //$("#newstitle").append("<div>" + storeArraynews[0][5] + "</div>");
                    var z=0;
                    ipp=ipp-6;
                    console.log(ipp)
                      for(k=0;k<storeArraynews.length;)
                       for(j=0;j<storeArraynews[k].length;j++){
                        //console.log(tlln)
                        $("<div />", { "class":"newsblock", id:"news"+z })
                         .append($("<a />", {  class:"n-a",id:"n-img-a"+z }))
                         .append($("<a />", {  class:"n-a",id:"n-title"+z }))
                         .append($("<div />", {  class:"n-pub",id:"n-pub"+z }))
                         .appendTo("#newsdiv");

                        // $("#newsdiv").append("<div>",{ "class":"wrapper", id:"product"+i } "<div>" + storeArraynews[i][0] + "</div><div>" + storeArraynews[i][3] + "</div><div>" + storeArraynews[i][1] + "</div>");

                        //$("#n-fullstory" + j).append("<div>" + storeArraynews[j+6][1] + "</div>");
                        $("#n-img-a" + z).append($("<img />", {  class:"n-img",id:"n-img"+z }));
                        $("#n-title" + z).append(storeArraynews[k][j]['title']);
                        $("#n-pub" + z).append("<div>" + storeArraynews[k][j]['pubdate'] + "</div>");
                        $("#n-img" + z).attr('src' , storeArraynews[k][j]['image']);
                        $("#n-img-a" + z).attr('href','/full_news/'+storeArraynews[k][j]['id']);
                        $("#n-title" + z).attr('href','/full_news/'+storeArraynews[k][j]['id']);
               //         $("#n-img-a" + j).prop("href" , "/fullnews/" + storeArraynews[j][4]);
                        console.log($("kuch aaya" )
                        var y=storeArraynews[j+6][2];



                        if(y=="http://timesofindia.indiatimes.com/photo/7787613.cms"){

                             $("#n-img" + j).attr('src','../static/img/pasaulis1.jpg');
                        }


                    }

                    loading=false;
                    $(".loading").remove();
                },
                error: function(){
                    alert("error loading news");
                }
            });
          $("#owl-example").owlCarousel({

      autoPlay:3000,
    //  navigation : true,
    //  navigationText : ["prev","next"],
          items:2,
      itemsDesktop:[980,2],
      //itemsDesktopSmall : [979,2]
      itemsDesktopSmall :[950,1],

      itemsTablet:[478,1],

  });

});


/**
 * Created by sony on 04-12-2015.
 */
