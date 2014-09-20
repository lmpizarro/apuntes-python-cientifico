var redis = require("redis"),
    client1 = redis.createClient(),
    msg_count = 0;

var io;
var connector;
var ioChannel = "messageFromHMI";

redis.debug_mode = false;

exports.runIo = function (io_){
  console.log ("INICIALIZADO WS hmiToRedis");
  io = io_;
  io.on('connection', function (socket) {
      connector = socket; 
      socket.on(ioChannel, function (data) {
         reference =  data.message.val;
         console.log("From HMI ....................",reference);
       
         client1.publish(ioChannel, String (reference));
      });
  });
}

