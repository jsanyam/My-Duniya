/**
 * Created by SANCHIT on 10/7/2015.
 */
        //storeArrayurl=new Array();
        var loading=true;
        bckgrnd = new Array();

        function loadtags() {
            var t=0;
            for(j=1;j<=14;j++){
                var article = $("#pt" + j + "info").text();

                console.log(article)
                $.ajax({
                    type: 'GET',
                    //url:"{{ url_for('.articles') }}",
                    url:"/" + article ,
                   // url:"/World",
                    //url:"/news.json",

                    success: function(data, textStatus, xhr) {
                        $.each(data['tag'], function(i, el){
                                bckgrnd[i] = el.image;
                        });


                        t=t+1;
                        $("#pt" + t).css('background-image','url(' + bckgrnd[t] + ')');
                        var y=$("#pt" + t).css("background-image");
                        console.log(y);
                        if(y=="url(http://timesofindia.indiatimes.com/photo/7787613.cms)") {
                            $("#pt" + t).css('background-image', 'url(../static/img/pasaulis1.jpg)');
                        }
                    },
                    error: function(){
                        alert("error loading news");
                    }
                });
            }
        }






         /*   function loadNowPlaying(){
                 $("#now_playing").load("now_playing.php");
            }
            setInterval(function(){loadNowPlaying()},5000);
            $("#Add").click(function(){
                console.log("reached");
                var user = {
                    Name: $name.val(),
                    Desc: $desc.val()
                };
                console.log(user.Name);
                $.ajax({
                    type: 'POST',
                    url: "/news/",
                    data: user,
                    success: function(newUser){
                        //$article.append("<li>" + newUser.name + "</li><li>" + newUser.desc + "</li><b r><br>");
                        console.log(newUser.name, newUser.desc);
                    },
                    error: function(){
                        alert("error saving data");
                    }
                });
            });
           */
        $(function(){
            //loadslider();

            loadtags();

            //load();
            document.getElementById("content").style.visibility = "hidden";
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
           // loadfullnews();

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
              $('#pt1').hover(function(){

                  $('#pt1info').css('background-color','white');
                  $('#pt1info').css('border-color','black');
                  $('#pt1info').css('color','black');

               },

                function(){
                    $('#pt1info').css('background-color','transparent');
                     $('#pt1info').css('border-color','white');
                      $('#pt1info').css('color','white');

                });
                $('#pt2').hover(function(){

                  $('#pt2info').css('background-color','white');
                  $('#pt2info').css('border-color','black');
                  $('#pt2info').css('color','black');

               },

                function(){
                    $('#pt2info').css('background-color','transparent');
                     $('#pt2info').css('border-color','white');
                      $('#pt2info').css('color','white');

                });
                $('#pt3').hover(function(){

                  $('#pt3info').css('background-color','white');
                  $('#pt3info').css('border-color','black');
                  $('#pt3info').css('color','black');

               },

                function(){
                    $('#pt3info').css('background-color','transparent');
                     $('#pt3info').css('border-color','white');
                      $('#pt3info').css('color','white');

                });
                $('#pt4').hover(function(){

                  $('#pt4info').css('background-color','white');
                  $('#pt4info').css('border-color','black');
                  $('#pt4info').css('color','black');

               },

                function(){
                    $('#pt4info').css('background-color','transparent');
                     $('#pt4info').css('border-color','white');
                      $('#pt4info').css('color','white');

                });
              $('#pt5').hover(function(){

                  $('#pt5info').css('background-color','white');
                  $('#pt5info').css('border-color','black');
                  $('#pt5info').css('color','black');

               },

                function(){
                    $('#pt5info').css('background-color','transparent');
                     $('#pt5info').css('border-color','white');
                      $('#pt5info').css('color','white');

                });
                $('#pt6').hover(function(){

                  $('#pt6info').css('background-color','white');
                  $('#pt6info').css('border-color','black');
                  $('#pt6info').css('color','black');

               },

                function(){
                    $('#pt6info').css('background-color','transparent');
                     $('#pt6info').css('border-color','white');
                      $('#pt6info').css('color','white');

                });
                $('#pt7').hover(function(){

                  $('#pt7info').css('background-color','white');
                  $('#pt7info').css('border-color','black');
                  $('#pt7info').css('color','black');

               },

                function(){
                    $('#pt7info').css('background-color','transparent');
                     $('#pt7info').css('border-color','white');
                      $('#pt7info').css('color','white');

                });
                $('#pt8').hover(function(){

                  $('#pt8info').css('background-color','white');
                  $('#pt8info').css('border-color','black');
                  $('#pt8info').css('color','black');

               },

                function(){
                    $('#pt8info').css('background-color','transparent');
                     $('#pt8info').css('border-color','white');
                      $('#pt8info').css('color','white');

                });
              $('#pt9').hover(function(){

                  $('#pt9info').css('background-color','white');
                  $('#pt9info').css('border-color','black');
                  $('#pt9info').css('color','black');

               },

                function(){
                    $('#pt9info').css('background-color','transparent');
                     $('#pt9info').css('border-color','white');
                      $('#pt9info').css('color','white');

                });
                $('#pt10').hover(function(){

                  $('#pt10info').css('background-color','white');
                  $('#pt10info').css('border-color','black');
                  $('#pt10info').css('color','black');

               },

                function(){
                    $('#pt10info').css('background-color','transparent');
                     $('#pt10info').css('border-color','white');
                      $('#pt10info').css('color','white');

                });
                $('#pt11').hover(function(){

                  $('#pt11info').css('background-color','white');
                  $('#pt11info').css('border-color','black');
                  $('#pt11info').css('color','black');

               },

                function(){
                    $('#pt11info').css('background-color','transparent');
                     $('#pt11info').css('border-color','white');
                      $('#pt11info').css('color','white');

                });
                $('#pt12').hover(function(){

                  $('#pt12info').css('background-color','white');
                  $('#pt12info').css('border-color','black');
                  $('#pt12info').css('color','black');

               },

                function(){
                    $('#pt12info').css('background-color','transparent');
                     $('#pt12info').css('border-color','white');
                      $('#pt12info').css('color','white');

                });
                $('#pt13').hover(function(){

                  $('#pt13info').css('background-color','white');
                  $('#pt13info').css('border-color','black');
                  $('#pt13info').css('color','black');

               },

                function(){
                    $('#pt13info').css('background-color','transparent');
                     $('#pt13info').css('border-color','white');
                      $('#pt13info').css('color','white');

                });
                $('#pt14').hover(function(){

                  $('#pt14info').css('background-color','white');
                  $('#pt14info').css('border-color','black');
                  $('#pt14info').css('color','black');

               },

                function(){
                    $('#pt14info').css('background-color','transparent');
                     $('#pt14info').css('border-color','white');
                      $('#pt14info').css('color','white');

                });

        });


