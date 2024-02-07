function sendProductComment(productId) {
    // Returns the text value
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get('/products/add-product-comment', {
        product_comment: comment,
        product_id: productId,
        parent_id: parentId,
    }).then(res => {
        $('#comments_area').html(res);
        $('#commentText').val('');
        $('#parent_id').val('');

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

function addProductToOrder(productId) {
    const productCount = $('#product-count').val();
    $.get('/cart/add-to-cart?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        });
    });
}

function removeOrderDetail(detailId) {
    $.get('/user/remove-cart-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}
