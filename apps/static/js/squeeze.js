function display(){
    try{
        const fetchArk =  getArk();
        const fetchSpy =  getSpy();
        const fetchQqq =  getQqq();
    }
    catch(err){
        console.log("ERROR",err)
    }
}

display()


async function getArk(){
    const arkUrl = "/api/arkconsolidate";
    const resArk = await fetch(arkUrl);
    const ark = await resArk.json();
    let arkCon = ark["data"]["consolidate"]
    let arkBreak= ark["data"]["breakout"]
    if (Object.keys(arkCon).length !== 0){
        console.log(ark["data"]["consolidate"])
        console.log(Object.keys(arkCon).length)

        const item=document.getElementById("conloop")
        const itemconst=document.getElementById("conpic")

        for(var i=1;i<Object.keys(arkCon).length+1;i++){
            // item.innerHTML+="<li>"+arkCon[i]+"-</li>"
            itemconst.innerHTML+="<li><img src="+"https://finviz.com/chart.ashx?t="+arkCon[i]+"&ty=c&ta=1&p=d&s=l/></li>"
        }

    }else{
        console.log("ARK NO CONSOLIDATE")
    }
    if (Object.keys(arkBreak).length !==0){
        console.log(ark["data"]["breakout"])
        console.log(Object.keys(arkBreak).length)

        const itembreak=document.getElementById("breakloop")
        const itembreakpic=document.getElementById("breakpic")


    }else{
        console.log("ARK NO BREAKOUT")       
    }
}

async function getQqq(){
    const qqqUrl= "/api/qqqconsolidate";
    const resQqq = await fetch(qqqUrl);
    const qqq = await resQqq.json();
    let qqqCon = qqq["data"]["consolidate"]
    let qqqBreak= qqq["data"]["breakout"]

    if (Object.keys(qqqCon).length !== 0){
        console.log(qqq["data"]["consolidate"])
        console.log(Object.keys(qqqCon).length)

        const item=document.getElementById("conloop")
        const itemconst=document.getElementById("conpic")


        for(var i=1;i<Object.keys(qqqCon).length+1;i++){
            // document.write(arkCon[i]+"</br>")
            // item.innerHTML+="<li>"+qqqCon[i]+"-</li>"
            itemconst.innerHTML+="<li><img src="+"https://finviz.com/chart.ashx?t="+qqqCon[i]+"&ty=c&ta=1&p=d&s=l/></li>"
        }


    }else{
        console.log("QQQ NO CONSOLIDATE")
    }
    if (Object.keys(qqqBreak).length !==0){
        console.log(qqq["data"]["breakout"])
        console.log(Object.keys(qqqBreak).length)

        const itembreak=document.getElementById("breakloop")
        const itembreakpic=document.getElementById("breakpic")


    }else{
        console.log("QQQ NO BREAKOUT")       
    }
}

async function getSpy(){
    const spyUrl = "/api/spyconsolidate";
    const spyQqq = await fetch(spyUrl);
    const spy = await spyQqq.json();
    let spyCon = spy["data"]["consolidate"]
    let spyBreak= spy["data"]["breakout"]

    if (Object.keys(spyCon).length !== 0){
        console.log(spy["data"]["consolidate"])
        console.log(Object.keys(spyCon).length)

        const item=document.getElementById("conloop")
        const itemconst=document.getElementById("conpic")


        for(var i=1;i<Object.keys(spyCon).length+1;i++){
            // item.innerHTML+="<li>"+spyCon[i]+"-</li>"
            itemconst.innerHTML+="<li><img src="+"https://finviz.com/chart.ashx?t="+spyCon[i]+"&ty=c&ta=1&p=d&s=l/></li>"
        }


    }else{
        console.log("SPY NO CONSOLIDATE")
    }
    if (Object.keys(spyBreak).length !==0){
        console.log(spy["data"]["breakout"])
        console.log(Object.keys(spyBreak).length)

        const itembreak=document.getElementById("breakloop")
        const itembreakpic=document.getElementById("breakpic")

        for(var i=1;i<Object.keys(spyBreak).length+1;i++){
            // itembreak.innerHTML+="<li>"+spyBreak[i]+"-</li>"
            itembreakpic.innerHTML+="<li><img src="+"https://finviz.com/chart.ashx?t="+spyBreak[i]+"&ty=c&ta=1&p=d&s=l/></li>"
        }

    }else{
        console.log("SPY NO BREAKOUT")       
    }
}