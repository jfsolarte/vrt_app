const resemble = require("./node_modules/resemblejs/resemble.js");
var fs=require('fs'); 
img =''
imgBase = ''
process.argv.forEach(function (val, index, array) {
    console.log(index + ': ' + val);

    if(index == 2){
        imgBase= val; 
    }

    if(index == 3){
        img= val; 
    }

});



fs.exists(img,function(exists){ 
    if(exists){ 

        var diff = resemble(imgBase)
        .compareTo(img)
        .onComplete(function(data) {
            console.log(data);
            fs.writeFile('myjsonfile.json',JSON.stringify(data),function(err){
                if(err) throw err;
            })
        });
        
    }else{ 
     console.log("no"); 
    } 
}); 

