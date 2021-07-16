const express = require('express');
const app = express();

app.get("/", function(req, res){
    // res.send("Seja bem vindo ao meu app")
    res.sendFile(__dirname + '/html/index.html'); //DIRNAME (directory name), pega a pasta onde esta o arquivo
})

app.get("/sobre", function(req, res){
    // res.send("Seja bem vindo a minha pagina sobre")
    res.sendFile(__dirname + "/html/sobre.html");
})

app.get("/blog", function(req, res){
    res.send("Bem vindo ao meu blog")
})

app.get("/ola/:nome/:cargo/:cor", function(req, res){
    res.send("<h1>Oi, " + req.params.nome + "</h1>"+ "<h2> Seu cargo e: " + req.params.cargo + "</h2>" +"<h3> Sua cor favorita e: "+ req.params.cor + "</h3>")
})

app.listen(9090, function () {
    console.log("Servidor rodando na url http://localhost:9090");
});
