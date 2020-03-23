let fs = require('fs'),
    PDFParser = require("pdf2json");

let pdfParser = new PDFParser();

pdfParser.on("pdfParser_dataError", errData => console.error(errData.parserError));
pdfParser.on("pdfParser_dataReady", pdfData => {
    const Pages = pdfData.formImage.Pages;

    console.log(Pages[0].Texts[0].R);
    // for(let i=0;i<Pages.length();i++){
    //     console.log(Pages[i]);
    // }
    // fs.writeFile("./pdf2json/test/F1040EZ.json", JSON.stringify(pdfData));
});

pdfParser.loadPDF("/Users/anusing/Downloads/ex.pdf");