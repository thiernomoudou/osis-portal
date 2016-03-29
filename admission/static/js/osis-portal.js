$("#slt_offer_type").change(function() {

    $("#pnl_grade_choices").find("label")
        .remove()
        .end()
    // Remove the offers
    $("#pnl_offers").find("table")
        .remove()
        .end()
    //Cancel the previous selection
    document.getElementById("txt_offer_year_id").value = "";

    document.getElementById("bt_save").disabled = true;
    var i=0;
    $.ajax({
        url: "/admission/levels?type=" + $("#slt_offer_type").val()
      }).then(function(data) {

        if(data.length >0){
        $.each(data, function(key, value) {

          $('#pnl_grade_choices').append($("<label></label>").attr("class", "radio-inline")
                                      .append($("<input>").attr("type","radio")
                                                                  .attr("name","grade_choice")
                                                                  .attr("value",value.id )
                                                                  .attr("id","grade_choice_"+value.id)
                                                                  .attr("onchange","offer_selection_display()"))
                                      .append(value.name));

        });
        }else{

        }
      });

});


$("#slt_domain").change(function() {

offer_selection_display();

});


function offer_selection_display(){
var radio_button_value;

           if ($("input[name='grade_choice']:checked").length > 0){
               radio_button_value = $('input[name="grade_choice"]:checked').val();
           }
           else{
               return False
           }

    $("#pnl_offers").find("table")
      .remove()
      .end()
    //Cancel the previous selection
    document.getElementById("txt_offer_year_id").value = "";

    document.getElementById("bt_save").disabled = true;

    var i=0;
    $.ajax({
        url: "/admission/offers?level=" + radio_button_value +"&domain="+$("#slt_domain").val()

      }).then(function(data) {
      var table_size=data.length;
      if(data.length >0){
        $('#pnl_grade_choices').append($("<table><tr><td></td></tr></table>"));
        var trHTML = '<table class="table table-striped table-hover">';
        trHTML += '<thead><th colspan=\'2\'><label>Cliquez sur votre choix d\'études</label></th></thead>';
        $.each(data, function(key, value) {
            id_str = "offer_row_" + i;

            onclick_str = "onclick=\'selection("+ i +", "+table_size+", " + value.id +")\'"
            trHTML += "<tr id=\'" +  id_str + "\' "+ onclick_str +"><td>"+ value.acronym + "</td><td>" + value.title + "</td></tr>";
            i++;
        });
        trHTML += '</table>'
        $('#pnl_offers').append(trHTML);
        }
      });
}


    function selection(row_number, offers_length, offer_year_id){
        var elt = "offer_row_" + row_number;
        var cpt = 0;
        var already_selected =new Boolean(false);
        while (cpt < offers_length ){
            elt = "offer_row_" + cpt;
            if (document.getElementById(elt).style.color == "green" && document.getElementById("txt_offer_year_id").value == offer_year_id){
                already_selected=new Boolean(true);
            }
            document.getElementById(elt).style.color = "black";
            cpt++;
        }
        elt = "offer_row_" + row_number;
                    document.getElementById(elt).style.color = "green";
            document.getElementById("txt_offer_year_id").value = offer_year_id;
            document.getElementById("bt_save").disabled = false;


        if(already_selected == true){
            document.getElementById(elt).style.color = "black";
            document.getElementById("txt_offer_year_id").value = "";
            document.getElementById("bt_save").disabled = true;
        }else{

            document.getElementById(elt).style.color = "green";
            document.getElementById("txt_offer_year_id").value = offer_year_id;
            document.getElementById("bt_save").disabled = false;
        }


    }