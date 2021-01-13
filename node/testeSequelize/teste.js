const Sequelize  = require('sequelize');
const sequelize = new Sequelize('teste', 'root', 'eportella313', {
    host: "localhost",
    dialect: 'mysql'
})

// sequelize.authenticate().then( function() {
//     console.log("Conectado com sucesso!")
// }).catch(function (erro) {
//     console.log("Falha ao se conectar: "+ erro)
// });

const Postagem = sequelize.define('postagens', {
  titulo: {
      type: Sequelize.STRING
  }, 
  conteudo: {
      type: Sequelize.TEXT
  }
})

Postagem.create({
    titulo: "Um titulo qualquer",
    conteudo: "lorem lorem lorem lorem eduudududu lorem lorem lorem lorem lorem"
})

// Postagem.sync({force: true})

const usuario =     sequelize.define('usuarios', {
    nome: {
        type: Sequelize.STRING
    },
    sobrenome: {
        type: Sequelize.STRING
    },
    idade: {
        type: Sequelize.INTEGER
    },
    email: {
        type: Sequelize.STRING
    }
})

usuario.create({
    nome: "Eduardo",
    sobrenome: "Portella",
    idade: 19,
    email: "eportella70@gmail.com"
})

// usuario.sync({force: true});