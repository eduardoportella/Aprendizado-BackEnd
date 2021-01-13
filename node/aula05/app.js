var http = require('http');

http.createServer(function(req, res){
    res.end("Voce teste")
}).listen(8081);
//F9 FECHA SERViDOR!!!!!!!!!!!!!

console.log("O servidor esta rodando!");