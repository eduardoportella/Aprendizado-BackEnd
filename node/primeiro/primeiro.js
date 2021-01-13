var http = require('http');
http.createServer(function (req, res){
    res.writeHead(200, {'Content-type': 'text/plain'});
    res.end("Ola mundo!, COE MENÓ");
}).listen(8080);
console.log('Servidor rodando em http://localhost:8080');   