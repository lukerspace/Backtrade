

async function GetData(number) {
  const url = "/api/arksign";
  const r = await fetch(url);
  const data = await r.json();
  const sell_url = "/api/arksignsell";
  const re = await fetch(sell_url);
  const selldata = await re.json();
  
  buy = data["data"];
  sell = selldata["data"];

  // 
  // const eps_url ="/api/arkeps";
  // const r_eps=await fetch(eps_url);
  // const epsdata = await r_eps.json();


  let title = document.getElementById("ticker");
  let date = document.getElementById("date");
  let pic = document.getElementById("img");
  let root = document.getElementById("root");
  let link=document.getElementById("link")


  let symbol = buy[number]["ticker"];

  let sellindex = [];
  for (i = 0; i < Object.keys(sell).length; i++) {
    sellindex.push(sell[i]["ticker"]);
  }
  
  const sell_date_exist = sellindex.findIndex((element) => element == symbol);
  if (sell_date_exist==-1){
  console.log("NO SellDate & SKIP : " +symbol)}
  if (sell_date_exist !==-1) {
    // console.log(sell_date_exist)
    const sell_date = sell[sell_date_exist]["date"];
    // console.log(sell_date)
    if (sell_date) {
    
      // text
      title.innerText = "TICKER : " + buy[number]["ticker"];
      
      // sinal_date
      date.innerText = "SIGNAL DATE : " + buy[number]["date"];
      pic.src = "https://finviz.com/chart.ashx?t=" + buy[number]["ticker"];
      root.innerText = "PREVIOUS SELL SIGNAL : " + sell_date;
      
      // ticker_chart
      let test = document.getElementById("test");
      test.src = "./static/png/" + buy[number]["ticker"] + ".png";
      
      // link
      link.href="/fundamental?symbol="+buy[number]["ticker"]

      return (size = Object.keys(buy).length) & (id = number);
    } else {
      console.log("SELL_DATE PROBLEM")
      //pass
    }
  } else {
    id=number
    GetData(id+1)
  }
}

function rankgo() {
  const getrank = document.getElementById("search");
  let rank = getrank.value;
  if (size) {
    if ((rank >= size) | (rank < 0)) {
      alert("OUT OF RANGE");
    } else {
      GetData(parseInt(rank));
    }
  } else {
    return console.log("wrong");
  }
}

function tickergo() {
  const findsymbol = document.getElementById("find").value.toUpperCase();
  ticklist = [];
  for (i = 0; i < Object.keys(buy).length; i++) {
    ticklist.push(buy[i]["ticker"]);
  }
  const tickindex = ticklist.findIndex((element) => element == findsymbol);
  if (tickindex !== -1) {
    GetData((number = tickindex));
  } else {
    alert("NO THIS TICKER");
  }
}
function nextgo() {
  const next = document.getElementById("next");
  if (id < size - 1) {
    GetData(id + 1);
  } else {
    alert("NO DATA");
  }
}

function prevgo() {
  const prev = document.getElementById("prev");
  if (id > 0) {
    GetData(id - 1);
  } else {
    alert("NO DATA");
  }
}

GetData(0);
