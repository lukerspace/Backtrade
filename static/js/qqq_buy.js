// let data = {};
async function GetData(number) {
  const url = "/api/qqqsign";
  const r = await fetch(url);
  const data = await r.json();

  const sell_url = "/api/qqqsignsell";
  const re = await fetch(sell_url);
  const selldata = await re.json();
  buy = data["data"];
  sell = selldata["data"];
  // console.log(buy);
  // console.log(buy)
  let title = document.getElementById("ticker");
  let date = document.getElementById("date");
  let pic = document.getElementById("img");
  let root = document.getElementById("root");
  let symbol = buy[number]["ticker"];

  let sellindex = [];
  for (i = 0; i < Object.keys(sell).length; i++) {
    sellindex.push(sell[i]["ticker"]);
  }
  const sell_date_exist = sellindex.findIndex((element) => element == symbol);
  if (sell_date_exist) {
    const sell_date = sell[sell_date_exist]["date"];
    if (sell_date) {
      // text
      title.innerText = "TICKER : " + buy[number]["ticker"];
      date.innerText = "SIGNAL DATE : " + buy[number]["date"];
      pic.src = "https://finviz.com/chart.ashx?t=" + buy[number]["ticker"];
      root.innerText = "Previous Sell Signal : " + sell_date;
      return (size = Object.keys(buy).length) & (id = number);
    } else {
      //pass
    }
  } else {
    return None;
  }
}

function rankgo() {
  const getrank = document.getElementById("search");
  let rank = getrank.value;
  if (size) {
    if ((rank > size) | (rank < 0)) {
      alert("out of range");
    } else {
      GetData(parseInt(rank));
    }
  } else {
    return none;
  }
}

function tickergo() {
  const findsymbol = document.getElementById("find").value;
  ticklist = [];
  for (i = 0; i < Object.keys(buy).length; i++) {
    ticklist.push(buy[i]["ticker"]);
  }
  const tickindex = ticklist.findIndex((element) => element == findsymbol);
  GetData((number = tickindex));
}

function nextgo() {
  const next = document.getElementById("next");
  if (id < size) {
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
