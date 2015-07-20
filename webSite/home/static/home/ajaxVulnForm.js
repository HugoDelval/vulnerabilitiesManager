var index_modifie = 0;

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function setupListeners() {

    $('select[id^="id_activites_liees_"]').on('change keyup', function(){
        index_modifie = $(this).attr('id').split('liees_')[1];
        $('#id_index_modifie').val(index_modifie);
        ajaxForm('#'+$(this).attr('id'));
    });

    $('#formulaire_recherche_vuln').on('submit', function(e){
        e.preventDefault();
        ajaxForm('#id_mot_clef');
    });
}

function ajaxForm(elementToFocusSelector){
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var form = $('#formulaire_recherche_vuln');
    $.ajax({
        method: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function(html){
            $('#ajax_writtable').html(html);
            setupListeners();
        },
        error: function(resultat, statut, erreur){
            $('#ajax_writtable').html("Désolé ! Une erreur serveur est survenue, veuillez réessayer.");
        }
    });
}

$(document).ready(function(){
    setupListeners();
});
