const express = require("express"); //const pra evitar erro de variável
const app= express();

app.get("/", function(req, res){
    res.sendFile(__dirname + "/html/index.html");
})

app.get("/sobre", function(req, res){
    res.sendFile(__dirname + "/html/sobre.html");
});

app.get("/blog", function(req, res){
    res.send("Bem vindo ao meu blog!");
})

app.get("/ola/:nome/:cargo/:cor", function(req, res){
    res.send("<h1>Ola " + req.params.nome + "</h1>" + "<h2>Seu cargo eh " + req.params.cargo + "</h2>" + "<h3>Sua cor favorita eh: " + req.params.cor + "</h3");
})

app.listen(8081, function() {
    console.log("servidor rodando");
}); //TEM DE SER A ULTIMA LINHA DO CÓDIGO