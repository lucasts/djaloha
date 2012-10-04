(function (window, undefined) {
    var Aloha = window.Aloha;

    Aloha.ready( function() {
        // Make #content editable once Aloha is loaded and ready.
        Aloha.jQuery('.djaloha-editable').aloha();
    });

    Aloha.bind('aloha-editable-deactivated', function(event, eventProperties){
        //Callback called when the fragment edition is done -> Push to the page
        var ed = eventProperties.editable;
        $("#"+ed.getId()+"_hidden").val($.trim(ed.getContents()));
    });

    var resize_thumbnail = function (the_obj) {

        $(".djaloha-editable img.djaloha-thumbnail").each(function(index) {
            $(this).removeClass("djaloha-thumbnail");
            $(this).attr("src", $(this).attr("rel"));
            $(this).removeAttr('rel');
        });

        $(".djaloha-editable a.djaloha-document").each(function(index) {

            var copy = $(this).clone();
            var img = copy.find("img");
            icon_url = img.attr('rel');
            doc_url = copy.attr('rel');
            doc_title = copy.attr('title');

            img.wrap('<div class="docdl_wrapper" />')
                .attr('src', icon_url)
                .removeClass('cms_doc_bloc')
                .addClass('doc_icon')
                .attr('alt', doc_title)
                .removeAttr('rel');

            var newdiv = copy.find("div.docdl_wrapper");
            newdiv.append('<a target="_blank" class="docdl_link" href="'+doc_url+'">'+doc_title+'</a>');

            copy.find("span.cms_doc_title").remove();
            newdiv.unwrap();
            newdiv.insertAfter($(this));
            $(this).remove();

        });

        //force the focus in order to make sure that the editable is activated
        //this will cause the deactivated event to be triggered, and the content to be saved
        the_obj.focus();
    }

    //resize image when dropped in the editor
    //GENTICS.Aloha.EventRegistry.subscribe(GENTICS.Aloha, 'editableCreated', function(event, editable) {
    Aloha.bind('aloha-editable-created', function(event, editable){
        var the_obj = editable.obj;
        jQuery(editable.obj).bind('drop', function(event){
            setTimeout(function() {
                    resize_thumbnail(the_obj);
            }, 100);
        });
    });

})(window);
