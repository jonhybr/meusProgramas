const Discord = require("discord.js");
const config = require("./config.json");
const client = new Discord.Client();

const low = require('lowdb')
const FileSync = require('lowdb/adapters/FileSync')
const adapter = new FileSync('db.json')
const db = low(adapter)


client.on("ready", () => {
  client.user.setActivity("Bot criado por jonhy. (!ajuda)")
})


client.on("guildCreate", () => {
  db.set(guild.id, []).write()
})



client.on("message", function(message){
  if (message.author.bot) return;
  if (!message.content.startsWith(config.prefix)) return;

  const commandBody = message.content.slice(config.prefix.length);
  const args = commandBody.split(' ');
  const command = args.shift().toLowerCase();

  if (command === "prefix"){
    if (!args[0]) return message.reply(`o prefixo atual é "${config.prefix}"`)
    else{
      config.prefix = args[0][0]
      message.reply(`o prefixo agora é "${config.prefix}"`)
    }
  }

  if (command === "ajuda"){
    console.log("ajuda")
    message.reply("Os comandos existentes atualmente são:" + `[${config.prefix}prefix, ${config.prefix}r]`)
  }
  
  if (command === "r"){
    d = args[0].search("d")    
    if (d === 0){
      let dado = args[0].replace('d', '')
      let num = Math.floor((Math.random() * dado) + 1)
      message.reply("`" + `d${dado}` + "` = " + `(${num}) = ${num}`)
    }
    if (d > 0){
      let dados = []
      let roladas = args[0].slice(0, d)
      let dado = args[0].slice(d + 1)
      let total = 0
      for (i = 0; i < roladas; i++){        
        resultado = Math.floor((Math.random() * dado) + 1)
        if (i > 0){
          dados.push(` ${resultado}`)
        }
        else{
          dados.push(`${resultado}`)
        }
        total += resultado
      }
      dados = dados.join()      
      message.reply("`" + `${roladas}d${dado}`+ "` = " + `(${dados}) = ${total}`)          
    }
  }
})

client.login(config.token)
