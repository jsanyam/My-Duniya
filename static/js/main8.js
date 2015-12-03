/**
 * Created by SANCHIT on 12/1/2015.
 */
/**
 * Created by SANCHIT on 10/7/2015.
 */
        //storeArrayurl=new Array();
        var loading=true;
        storeArray= new Array();
        storeArraynews= new Array();
        storeArrayfullnews= new Array();
        bckgrnd = new Array();

        var frmn=0;
        var tlln=9;

        function loadnews(){
            var $article = $("#articles");
            var $name = $("#name");
            var $desc = $("#desc");
            var x = $(location).attr('href');
            //console.log(x)
            var y=x.split('/');
            var l= y.length;
            //console.log(y[l-2])


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


          storeArray=new Array();

         $.ajax({
                type:'GET',
                url:"/" +y[l-1],
                success:function(data, textStatus, xhr) {
                    console.log(data);

                    $.each(data['tag'], function(i, el)
                    {

                        storeArray[i]=new Array(el.title, el.category,el.image,el.id);

                    });

                    	for(i=1;i<7;i++)
                    	{
                    		$(".content" + i + " " + "h1").text(storeArray[i-1][0]);

                    	}


                    	for(i=1;i<7;i++)
                    	{
                                var x = storeArray[i-1][1];
                                var x = x.split("-").join(" ");
                                $(".content" + i + " " + "h2").text(x);

                            if(storeArray[i-1][1]=="The Logical Indian"){
                                    $(".content" + i + " " + "h2").css("width","170px");
                            }
                            if(storeArray[i-1][1]=="fashion-and-trends"){
                                    $(".content" + i + " " + "h2").css("width","180px");
                            }
                            if(storeArray[i-1][1]=="sex-and-relationships"){
                                    $(".content" + i + " " + "h2").css("width","210px");
                            }
                            if(storeArray[i-1][1]=="art-and-culture"){
                                    $(".content" + i + " " + "h2").css("width","160px");
                            }
                    	}



                    	for(i=1;i<7;i++)
                    	{
                            console.log("imagine")
                    		$(".content" + i + " " + "img").attr("src",storeArray[i-1][2]);

                    	}


                        for(i=1;i<7;i++)
                    	{
                    		$("#a" + i).attr('href','/full_news/'+storeArray[i-1][3]);

                    	}


                    	for(i=1;i<7;i++)
                    	{
                    		$(".content" + i + " " + ".b1").attr('href','/tagnews/'+storeArray[i-1][1]);

                    	}




                   /* 	for(i=1;i<9;i++)
                    	{
                    	 if(!storeArray[i-1][2] || storeArray[i-1][2]=="http://timesofindia.indiatimes.com/photo/7787613.cms")
                    	 {
                            $(".content" + i + " " + "img").attr('src','../static/img/header.png');
                         }

                         else
                         {
                    		$(".content" + i + " " +"img").attr("src",storeArray[i-1][2]);
                   	/* 		$(".content2 img").attr("src",storeArray[1][2]);
                    		$(".content3 img").attr("src",storeArray[2][2]);
                    		$(".content4 img").attr("src",storeArray[3][2]);
                    		$(".content5 img").attr("src",storeArray[4][2]);
                    		$(".content6 img").attr("src",storeArray[5][2]);
                    		$(".content7 img").attr("src",storeArray[6][2]);
                    		$(".content8 img").attr("src",storeArray[7][2]);
                    		$(".content9 img").attr("src",storeArray[8][2]);
                    		$(".content10 img").attr("src",storeArray[9][2]);

                    	}


                    }

                    */
                 //   for(i=frm;i<tll;i++){
                    //    console.log(storeArray[i][0]);
                      //  console.log(storeArray[i][1]);
                   //    $("#result").append("<div>" + storeArray[i][0] + "</div>");
                    //    $("#result").append("<div>" + storeArray[i][1] + "</div><br><br>");
                   // }

                },
                error: function(){
                    alert("error loading news");
                }
            });



            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/" + y[l-1],
                success: function(data, textStatus, xhr) {
                    //console.log(data);
                    $.each(data['tag'], function(i, el){
                        console.log(el.title);
                        storeArraynews[i]=new Array(el.title, el.description,el.image,el.pubdate,el.id, el.category);
                    });
                    console.log(storeArraynews[1][5])
                     var x = storeArraynews[1][5];
                     var x = x.split("-").join(" ");
                     $("#heading").append("<div>" + x + "</div>");-
                    //console.log("pahuche")
                    $("#newstitle").append("<div>" + storeArraynews[0][5] + "</div>");
                    for(j=frmn;j<tlln;j++){
                       // console.log(frmn)
                        //console.log(tlln)
                        $("<div />", { "class":"newsblock", id:"news"+j })
                         .append($("<a />", {  class:"n-a",id:"n-img-a"+j }))
                         .append($("<a />", {  class:"n-a",id:"n-title"+j }))
                         .append($("<div />", {  class:"n-pub",id:"n-pub"+j }))
                         .appendTo("#newsdiv");

                        // $("#newsdiv").append("<div>",{ "class":"wrapper", id:"product"+i } "<div>" + storeArraynews[i][0] + "</div><div>" + storeArraynews[i][3] + "</div><div>" + storeArraynews[i][1] + "</div>");

                        //$("#n-fullstory" + j).append("<div>" + storeArraynews[j+6][1] + "</div>");
                        $("#n-img-a" + j).append($("<img />", {  class:"n-img",id:"n-img"+j }));
                        $("#n-title" + j).append(storeArraynews[j+6][0]);
                        $("#n-pub" + j).append("<div>" + storeArraynews[j+6][3] + "</div>");
                        $("#n-img" + j).attr('src' , storeArraynews[j+6][2]);
                        $("#n-img-a" + j).attr('href','/full_news/'+storeArraynews[j+6][4]);
                        $("#n-title" + j).attr('href','/full_news/'+storeArraynews[j+6][4]);
               //         $("#n-img-a" + j).prop("href" , "/fullnews/" + storeArraynews[j][4]);
                        console.log($("#n-img-a"+j).attr('href') )
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



        }






        $(function(){

            loadnews();


            $("#newstag").scroll(function(){
                var curScroll = $(this)[0].scrollTop;
                var maxScroll = $(this)[0].scrollHeight- $(this).height();

                console.log(curScroll);
                console.log(maxScroll);
                console.log(loading);
                console.log("yahaan pahuche5");
                if((curScroll >= maxScroll - 400) && loading == false){
                    loading = true;
                    console.log("yahaan?")
                    frmn=tlln;
                    tlln += 9;
                    //$("#live_buzz").append("<div class='.loading'>loading</div>");
                    $(this)[0].scrollTop = $(this)[0].scrollHeight- $(this).height();
                    loadnews();
                }
            });

        });


/**
 * Created by SANCHIT on 12/1/2015.
 */
/**
 * Created by SANCHIT on 12/1/2015.
 */
/**
 * Created by SANCHIT on 12/1/2015.
 */
