var http = require('http');
// var http = require('fs'); arquivos

http.createServer(function(req, res){
    res.end("ooi")
}).listen(9090);
console.log("Servidor rodando!")