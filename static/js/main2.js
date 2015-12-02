/**..Created by SANCHIT on 10/7/2015..**/
        var loading=true;
        storeArray= new Array();
        storeArraynews= new Array();
        storeArrayfullnews= new Array();
        bckgrnd = new Array();

        function loadfullnews(){
            var $article = $("#articles");
            var $name = $("#name");
            var $desc = $("#desc");
           // var x = $(location).attr('href');
            //console.log(x)
            //var y=x.split('/');
            //var l= y.length;
            //console.log(y[l-2])

            var x = $(location).attr('href');
            console.log(x);
            var y=x.split('/');
            var l= y.length;
            console.log(y[l-1]);
            var z=y[l-1];
            console.log(z);
            $.ajax({
                type: 'GET',
                //url:"{{ url_for('.articles') }}",
                url:"/news.json/" + z,
                success: function(data, textStatus, xhr) {
                    console.log(data);
                    console.log(data['article'][0].title);


                    console.log("pahuche");

                    $("<div />", { "class":"fnewsblock", id:"fnews" })
                         .append($("<div />", {  class:"fn-title",id:"fn-title" }))
                         .append($("<div />", {  class:"fn-img",id:"fn-img" }))
                         .append($("<div />", {  class:"fn-pub",id:"fn-pub" }))
                         .append($("<div />", {  class:"fn-fullstory",id:"fn-fullstory" }))
                         .appendTo("#fnewsdiv");
                    console.log(data['article'][0].title)
                    console.log(data['article'][0].fullnews)
                    console.log(data['article'][0].pubdate)
                    console.log(data['article'][0].image)
                    var x=data['article'][0].full_story;
                    var y= x.split("\n").join("<br>");
                    $("#fnewstitle").append("<div>" + data['article'][0].category + "</div>")
                    $("#fn-fullstory").append("<div>" + y + "</div>") ;
                    $("#fn-title").append("<div>" + data['article'][0].title + "</div>") ;
                    $("#fn-pub").append("<div>" + data['article'][0].pubdate + "</div>");
                    $("#fn-img").css('background-image','url(' + data['article'][0].image + ')');
                    $("#heading").append("<div>" + data['article'][0].category + "</div>");
                    var $y = $("#fn-img").css('background-image');
                    console.log(y);

                },
                error: function(){
                    alert("error loading news");
                }
            });
        }







        $(function(){
            //loadslider();

            //loadtags();

            //load();
            //document.getElementById("#content").style.visibility = "hidden";
            //$(".p-tags").click(function() {
              //   document.getElementById("newstag").style.visibility = "block";

//            });
            /*
            $("#live_buzz").scroll(function(){
                var curScroll = $(this)[0].scrollTop;
                var maxScroll = $(this)[0].scrollHeight- $(this).height();

                console.log(curScroll);
                console.log(maxScroll);
                console.log(loading);
                //console.log("yahaan pahuche2");
                if((curScroll >= maxScroll - 400) && loading == false){
                    loading = true;
                    frm=tll;
                    tll += 3;
                    //$("#live_buzz").append("<div class='.loading'>loading</div>");
                    $(this)[0].scrollTop = $(this)[0].scrollHeight- $(this).height();
                    //load();
                }
            });
               */
            //loadnews();
            loadfullnews();



        });


