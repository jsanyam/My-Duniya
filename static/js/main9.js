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
                    console.log("pahuche");

                    console.log(data['article'][0].category)
                    if(data['article'][0].category=="The Logical Indian"){
                        var x = data['article'][0].category;
                        var x = x.split("-").join(" ");
                        $("<div />", { "class":"fnewsblock", id:"fnews" })
                             .append($("<div />", {  class:"fn-title",id:"fn-title" }))
                             .append($("<div />", {  class:"fn-img",id:"fn-img" }))
                             .append($("<div />", {  class:"fn-pub",id:"fn-pub" }))
                             .append($("<div />", {  class:"fn-fullstory",id:"fn-fullstory" }))
                                .appendTo("#fnewsdiv");
                        console.log(data['article'][0].category)
                        $("#fn-fullstory").append("<div>" + data['article'][0].html + "</div>");
                        $("#fn-title").append("<div>" + data['article'][0].title + "</div>");
                        $("#fn-pub").append("<div>" + data['article'][0].pubdate + "</div>");
                        $("#fn-img").css('background-image', 'url(' + data['article'][0].image + ')');
                        $("#heading").append("<div>" + x + "</div>");
                    }
                    else if(data['article'][0].category=="TechCrunch" || data['article'][0].category=="YourStory"){
                        var x = data['article'][0].category;
                        var x = x.split("-").join(" ");
                        $("<div />", { "class":"fnewsblock", id:"fnews" })
                             .append($("<div />", {  class:"fn-title",id:"fn-title" }))
                             .append($("<div />", {  class:"fn-pub",id:"fn-pub" }))
                             .append($("<div />", {  class:"fn-fullstory",id:"fn-fullstory" }))
                                .appendTo("#fnewsdiv");
                        console.log(data['article'][0].category)
                        $("#fn-fullstory").append("<div>" + data['article'][0].html + "</div>");
                        $("#fn-title").append("<div>" + data['article'][0].title + "</div>");
                        $("#fn-pub").append("<div>" + data['article'][0].pubdate + "</div>");
                        $("#heading").append("<div>" + x + "</div>");
                    }
                    else {
                        $("<div />", { "class":"fnewsblock", id:"fnews" })
                             .append($("<div />", {  class:"fn-title",id:"fn-title" }))
                             .append($("<div />", {  class:"fn-img",id:"fn-img" }))
                             .append($("<div />", {  class:"fn-pub",id:"fn-pub" }))
                             .append($("<div />", {  class:"fn-fullstory",id:"fn-fullstory" }))
                                .appendTo("#fnewsdiv");
                        var x = data['article'][0].category;
                        var x = x.split("-").join(" ");
                        var y = data['article'][0].full_story;
                        var y = y.split("\n").join("<br><br>");
                        var y = y.split("<br><br><br><br><br><br>").join("<br><br>");
                        var y = y.split("<br><br><br><br>").join("<br><br>");
                        var y = y.split("<br><br><br><br>").join("<br><br>");
                        $("#fn-fullstory").append("<div>" + y + "</div>");
                        $("#fn-title").append("<div>" + data['article'][0].title + "</div>");
                        $("#fn-pub").append("<div>" + data['article'][0].pubdate + "</div>");
                        $("#fn-img").css('background-image', 'url(' + data['article'][0].image + ')');
                        $("#heading").append("<div>" + x + "</div>");
                    }
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


/**
 * Created by SANCHIT on 12/1/2015.
 */
