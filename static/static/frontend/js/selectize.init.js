$('#select-country').selectize();
$('#select-category').selectize({
    create: true,
    sortField: {
        field: 'text',
        direction: 'asc'
    },
    dropdownParent: 'body'
});