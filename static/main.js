/**
 * Created by sony on 25-09-2015.
 */
$(document).ready(function(){
        var $article = $("#articles");
        var $name = $("#name");
        var $desc = $("#desc");
        $.ajax({
            type: 'GET',
            //url:"{{ url_for('.articles') }}",
            url:"/news/",
            success: function(data, textStatus, xhr) {
                console.log(data);
                $.each(data['articles'], function(i, el){
                    $article.append("<li>" + el.title + "</li><li>" + el.full_story + "</li><br><br>");
                });
            },
            error: function(){
                alert("error loading news");
            }
        });
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
});