function getContent(category){
    if ( $(`#${category}-contentContainer`).children().length > 0 ) {
       return;
    }

    var url = `/${category}/`;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Accept', 'application/json');


    let container = $(`#${category}-contentContainer`).parent();
    container.addClass('loading');
    container.find('.fa-circle-notch').toggleClass('hidden');

    xhr.addEventListener('readystatechange', function(e) {
        if (xhr.readyState == 4 && xhr.status == 200) {
        var response = JSON.parse(xhr.response);
        createCategoryItems(category, response);

        let container = $(`#${category}-contentContainer`).parent();
        container.find('.fa-circle-notch').toggleClass('hidden');
        container.removeClass('loading');
        }
        else {
            console.error('errors')
        }
    });
    xhr.send();
}

var createCategoryItems = function(category, data){
    let contentContainerContainer = $(`#${category}-contentContainer`);
    contentContainerContainer.removeClass('hidden');
    data.result.forEach(function (item, index) {
        let itemContainer = $('<div>').addClass('item-container flex');
        let rightContainer = $('<div>').addClass('right-container');
        let leftContainer = $('<div>').addClass('left-container');
        let img = $('<img/>').attr('src', item.icon_url);
        let position = index + 1;
        let head = $('<p/>').html(`${position}: ${item.value}`);
        rightContainer.append(head);
        leftContainer.append(img);
        itemContainer.append(leftContainer);
        itemContainer.append(rightContainer);
        contentContainerContainer.append(itemContainer);
    });
}

var closeJokesContainer = function(event, category){
    if ( $(`#${category}-contentContainer`).children().length > 0 ) {
        let contentContainerContainer = $(`#${category}-contentContainer`);
        contentContainerContainer.toggleClass('hidden');
        $(event.target).toggleClass('fa-angle-down fa-angle-up');
    }

}