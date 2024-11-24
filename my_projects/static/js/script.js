// Confirmation before submitting the form
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    if (form) {
        form.addEventListener('submit', function(event) {
            const isConfirmed = confirm('Are you sure you want to submit the form?');
            if (!isConfirmed) {
                event.preventDefault();  // Prevent the form from submitting
            }
        });
    }
});
