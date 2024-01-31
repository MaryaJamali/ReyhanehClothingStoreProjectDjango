function sendProductComment(productId) {
    // Returns the text value
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get('/products/add-product-comment', {
        product_comment: comment,
        product_id: productId,
        parent_id: parentId
    }).then(res => {
        $('#commentText').val('');
        $('#parent_id').val('');
        location.reload();

        if (parentId !== null && parentId !== '') {
            document.getElementById('single_comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comments_area').scrollIntoView({behavior: "smooth"});
        }
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    // Click "answer" to come to the text section
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}
