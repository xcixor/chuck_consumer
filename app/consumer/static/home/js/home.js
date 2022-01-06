function getContent(category){
  var url = `/${category}/`;

  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var response = JSON.parse(xhr.response);
        createCategoryItems(category, response);
    }else {
        var errors = xhr.status;
        console.error(errors)
    }
    };
  xhr.send();
}

var createCategoryItems = function(category, data){
    let contentContainerContainer = $(`#${category}-contentContainer`);
    data.result.forEach(function (item, index) {
        console.log(item)
        let itemContainer = $('<div>').addClass('item-container flex');
        let rightContainer = $('<div>').addClass('right-container');
        let leftContainer = $('<div>').addClass('left-container');
        let img = $('<img/>').attr('src', item.icon_url);
        let head = $('<p/>').html(`item: ${item.id}`);
        rightContainer.append(head);
        leftContainer.append(img);
        itemContainer.append(leftContainer);
        itemContainer.append(rightContainer);
        contentContainerContainer.append(itemContainer);
    });
}

$('.category-card').on('click', function(){
    $('.category-content').toggleClass('hidden');
})