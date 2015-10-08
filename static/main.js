/**
 * Created by sony on 25-09-2015.
 */
$(document).ready(function(){

     storearray=new Array();

    $.ajax({

        type:'GET',
        url:'/Lifestyle',
        success:function(data,textstatus,xhr) {

            $.each(data['tag'], function(i, el)
            {

                storearray[i] = new Array(el.title,el.description,el.image);

            });


            $("#r1c2").append("<div id='tag1'>" + storearray[0][0]+ "</div>");
            $("#r1c2").append("<div id='tagg1'>" + storearray[0][0]+ "</div>");
            $("#r1c2").css('background-image','url(' + storearray[0][2] + ')');
            $("#r1c2").css('background-size','100% 100%');
            //$("#r1c2").append("<div>" + storearray[0][1] + "</div>");
            //$("#r1c2").append("<div>" + storearray[1][0] + "</div>");
            $('#tag1').css('background-color','rgba(84,84,84,0.6)');

            //$('#tag1').css('font-family','Lucida Grande,sans-serif');
            $('#r1c2').css('filter','brightness(65%)');
            $('#tagg1').css('background-color','rgba(0,0,0,0.7)');
            //$('#tagg1').css('font-style','italic');
            $('#tagg1').css('margin-top','150px');
            $('#tagg1').css('margin-left','20px');
            $('#tagg1').css('margin-right','20px');
             $('#tag1').css('text-align','center');
             $('#tag1').css('color','white');
             $('#tag1').css('margin-top','20px');
             $('#tag1').css('font-size','25px');
             $('#tagg1').css('font-size','17px');

             $('#tagg1').css('color','white');
        },

        error:function(){

            alert("error loading news");
        }


    });

        twoarray=new Array();

            $.ajax({

        type:'GET',
        url:'/Technology',
        success:function(data,textstatus,xhr) {

            $.each(data['tag'], function(i, el)
            {

                twoarray[i] = new Array(el.title,el.description,el.image);

            });


            $("#r2c1").append("<div id='tag2'>" + twoarray[0][0]+ "</div>");
            $("#r2c1").append("<div id='tagg2'>" + twoarray[0][1]+ "</div>");
            $("#r2c1").css('background-image','url(' + twoarray[0][2] + ')');
            $("#r2c1").css('background-size','100% 100%');

            //$("#r1c2").append("<div>" + storearray[0][1] + "</div>");
            //$("#r1c2").append("<div>" + storearray[1][0] + "</div>");
              $('#tag2').css('background-color','rgba(84,84,84,0.6)');
              $('#tagg2').css('background-color','rgba(0,0,0,0.7)');
            //$('#tag2').css('background-color','grey');
            //$('#tagg2').css('background-color','grey');
           // $('#tag2').css('font-family','Lucida Grande,sans-serif');
            $('#r2c1').css('filter','brightness(65%)');
            //$('#tagg2').css('font-style','italic');
            $('#tagg2').css('margin-top','150px');
            $('#tag2').css('margin-top','20px');
            $('#tagg2').css('margin-left','20px');
            $('#tagg2').css('margin-right','20px');
             $('#tag2').css('text-align','center');
            $('#tag2').css('color','white');
             $('#tagg2').css('color','white');
             $('#tag2').css('font-size','25px');
             $('#tagg2').css('font-size','17px');

        },

        error:function(){

            alert("error loading news");
        }



    });




             threearray=new Array();

            $.ajax({

        type:'GET',
        url:'/Top stories',
        success:function(data,textstatus,xhr) {

            $.each(data['tag'], function(i, el)
            {

                threearray[i] = new Array(el.title,el.description,el.image);

            });


            $("#r3c1").append("<div id='tag3'>" + threearray[0][0]+ "</div>");
            $("#r3c1").append("<div id='tagg3'>" + threearray[0][1]+ "</div>");
            $("#r3c1").css('background-image','url(' + threearray[0][2] + ')');
            $("#r3c1").css('background-size','100% 100%');
            //$("#r1c2").append("<div>" + storearray[0][1] + "</div>");
            //$("#r1c2").append("<div>" + storearray[1][0] + "</div>");
             $('#tag3').css('background-color','rgba(84,84,84,0.6)');
              $('#tagg3').css('background-color','rgba(0,0,0,0.7)');
            //$('#tag3').css('background-color','grey');
            //$('#tagg3').css('background-color','grey');
           // $('#tag3').css('font-family','Lucida Grande,sans-serif');
              $('#r3c1').css('filter','brightness(65%)');
            //$('#tagg3').css('font-style','italic');
            $('#tagg3').css('margin-top','150px');
            $('#tag3').css('margin-top','20px');
            $('#tagg3').css('margin-left','20px');
            $('#tagg3').css('margin-right','20px');
             $('#tag3').css('text-align','center');
            $('#tag3').css('color','white');
             $('#tagg3').css('color','white');
             $('#tag3').css('font-size','25px');
             $('#tagg3').css('font-size','17px');

        },

        error:function(){

            alert("error loading news");
        }



    });



             fourarray=new Array();

            $.ajax({

        type:'GET',
        url:'/Entertainment',
        success:function(data,textstatus,xhr) {

            $.each(data['tag'], function(i, el)
            {

                fourarray[i] = new Array(el.title,el.description,el.image);

            });


            $("#r4c2").append("<div id='tag4'>" + fourarray[0][0]+ "</div>");
            $("#r4c2").append("<div id='tagg4'>" + fourarray[0][1]+ "</div>");
            $("#r4c2").css('background-image','url(' + fourarray[0][2] + ')');
            $("#r4c2").css('background-size','100% 100%');
            //$("#r1c2").append("<div>" + storearray[0][1] + "</div>");
            //$("#r1c2").append("<div>" + storearray[1][0] + "</div>");
             $('#tag4').css('background-color','rgba(84,84,84,0.6)');
              $('#tagg4').css('background-color','rgba(0,0,0,0.7)');
            //$('#tag4').css('background-color','grey');
            //$('#tagg4').css('background-color','grey');
            //$('#tag4').css('font-family','Lucida Grande','sans-serif');
            $('#r4c2').css('filter','brightness(65%)');
          //  $('#tagg4').css('font-style','italic');
            $('#tagg4').css('margin-top','150px');
            $('#tag4').css('margin-top','20px');
            $('#tagg4').css('margin-left','20px');
            $('#tagg4').css('margin-right','20px');
            $('#tag4').css('text-align','center');
            $('#tag4').css('color','white');
            $('#tagg4').css('color','white');
             $('#tag4').css('font-size','25px');
             $('#tagg4').css('font-size','17px');

        },

        error:function(){

            alert("error loading news");
        }



    });



});

      /*  $("#Add").click(function(){
            console.log("reached");
            var user = {
                Name: $name.val(),
                Desc: $desc.val()
            };
            console.log(user.Name);
            $.ajax({
                type: 'POST',
                url: "/news.json/",
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

});
          */