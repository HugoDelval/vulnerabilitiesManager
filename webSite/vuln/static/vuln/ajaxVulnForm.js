
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
    $('select#mots_clefs_choice').select2({
        width: '100%'
    });

    $('select#mots_clefs_choice')
        .select2({
            tags: true,
            placeholder: 'Choisis tes mots clefs !',
            width: '100%',
            matcher: function (params, data) {
                // If there are no search terms, return all of the data
                if ($.trim(params.term) === '') {
                    return data;
                }
                // `params.term` should be the term that is used for searching
                // `data.text` is the text that is displayed for the data object
                if (data.text.toLowerCase().replace("-", "").indexOf(params.term.toLowerCase().replace("-", "")) > -1) {
                    return $.extend({}, data, true);
                }

                // Return `null` if the term should not be displayed
                return null;
            }
        })
        .on('change keyup', function(){
            ajaxForm();
        });

    $('select[id^="id_activites_liees_"]').on('change keyup', function(){
        index_modifie = $(this).attr('id').split('liees_')[1];
        $('#id_index_modifie').val(index_modifie);
        ajaxForm();
    });

    $('#formulaire_recherche_vuln').on('submit', function(e){
        e.preventDefault();
        ajaxForm();
    });
}

function ajaxForm(){
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var form = $('#formulaire_recherche_vuln');
    var mots_clefs = "";
    form.find("#mots_clefs_choice").find("option:selected").each(function () {
        var $this = $(this);
        var nom = $this.text();
        if (nom.length) {
            mots_clefs += nom + "-";
        }
    });
    $('#id_mots_clefs').val(mots_clefs);

    $.ajax({
        method: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function(html){
            $('#ajax_writtable').html(html);
            setupListeners();
            $("span.select2-container--open").removeClass('select2-container--open');
            $("span.select2-container--open").removeClass('select2-container--close');
        },
        error: function(resultat, statut, erreur){
            $('#ajax_writtable').html("Désolé ! Une erreur serveur est survenue, veuillez réessayer.");
        }
    });
}

$(document).ready(function(){
    setupListeners();
});
