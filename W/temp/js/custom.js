var flag =0
var c=0
function handleFile(elem)
    {
        file_name = elem.files[0].name;
        //alert(file_name);
        file_name = file_name.substring(file_name.lastIndexOf(".") + 1);
        if(file_name != "txt" && file_name != "fasta" && file_name != undefined){
            flag = 1;
            alert("The upload file must be txt or fasta file.");
            return false;
        }
        flag = 0;

    }


function timedCount() {
if(flag == 0)
	{
            document.getElementById('time').value=c;
 	    c=c+1;
 	    t=setTimeout("timedCount()",1000);
 	    document.getElementById('txtt').style.visibility="visible";
 	    return true;
        }
        else if(flag == 1)
        {
            alert("Sorry, the upload file must be txt or fasta file.");
            return false;
        }
}


