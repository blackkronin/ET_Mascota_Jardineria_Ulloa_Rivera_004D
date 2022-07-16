$(function(){
    $('button.delete').on('click',function(event){
        var me      = $(this),
            form    = me.parents('form'),
            title   = me.data('title') || 'Make this change?';
        event.preventDefault();
        openActionDialog({
            message     : title,
            parent      : form[0].id
        });
    });
  
  $('#normal-dialog').on('click',function(event){
        openDialog({
            noerror     : true,
            message     : '<div class="lead text-center">This dialog has a width and height set when created.</div>',
            width       : window.innerWidth -20,
            height      : window.innerHeight - 60,
        });
    });
  
  $('#action-dialog').on('click',function(event){
        openActionDialog({
            noerror     : true,
            message     : 'Are you sure you want to process the callback?',
          callback : function(m){
            alert('Something could happen in here.');
            m.modal('hide');
          }
        });
    });
});