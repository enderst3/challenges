'use strict'

$(document).ready(function(){
    
    
    function format_info(users){
        
        for (var i = 0; i < users.length; i++){
            
            var user = users[i]
            var title = user.name.title
            var first = user.name.first
            var last = user.name.last
            var email = user.email
            var cell = user.cell
            var gender = user.gender 
            var dob = user.dob.slice(0,11) 
            var image = user.picture.medium 
            
            var $output = $('<div class="col-md-8" id="8"><div class="well">'+"<img src='"+image+"', class'img-thumbnail' alt='thumb' width= '100' height = '125'>"+'<div id="name"><a>'+'Name: '+title+' '+' '+first+' '+last+'</a></div><div id="gender"><a>Gender: '+gender+'</a></div><div id="dob"><a>Date of Birth: '+dob+'</a></div><div id="cell"><a>Cell: '+cell+'</a></div><div id="email"><a>Email: '+email+"</a></div></div></div>");
            
            $('.row').append($output)
        }
        
    };
    
    $.ajax({url: 'https://api.randomuser.me',
            
            type: 'GET',
            
            data: {results: '5'},
            
            success: function(response){
                console.log(response);
                format_info(response.results);
            },

            error: function(error){
                alert(error);
            },
        
    });
    
});