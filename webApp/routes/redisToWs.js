var redis = require("redis"),
    client1 = redis.createClient(),
    msg_count = 0;

var io;
var connector;
var ioChannel = "rtChannel";

redis.debug_mode = false;

client1.on("psubscribe", function (pattern, count) {
    console.log("client1 psubscribed to " + pattern + ", " + count + " total subscriptions");
});

client1.on("punsubscribe", function (pattern, count) {
    console.log("client1 punsubscribed from " + pattern + ", " + count + " total subscriptions");
    client1.end();
});

client1.on("pmessage", function (pattern, channel, message) {
  //console.log("("+  pattern +")" + " client1 received message on " + channel + ": " + message);
   msg_count += 1;
   if (message != null){
      //console.log (message);
      obj = JSON.parse(message);
      if (typeof connector != "undefined"){
        connector.emit(ioChannel, { message: obj });
        //console.log ("EMITING", ioChannel);
      }
   }
});

client1.psubscribe("SysControlFB");

exports.runIo = function (io_){
  console.log ("INICIALIZADO WS redisToWs");
  io = io_;
  io.on('connection', function (socket) {
      connector = socket; 
      connector.emit(ioChannel, { message: 'connected' });
  });
}

