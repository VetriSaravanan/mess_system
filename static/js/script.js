document.addEventListener('DOMContentLoaded', function() {
    // Form validation for all forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const inputs = form.querySelectorAll('input, textarea, select');
            let valid = true;

            inputs.forEach(input => {
                if (input.value.trim() === '') {
                    input.style.borderColor = 'red';
                    valid = false;
                } else {
                    input.style.borderColor = '#ccc';
                }
            });

            if (!valid) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    });

    // AJAX for real-time data updates (e.g., meal plans, attendance)
    const updateButtons = document.querySelectorAll('.ajax-update');
    updateButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const url = button.dataset.url; // Data URL for AJAX call
            const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    action: button.dataset.action,
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Update successful!');
                    // Update DOM or refresh data
                } else {
                    alert('Update failed. Try again.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    // Dynamic content for notification updates
    const notificationBell = document.querySelector('.notification-bell');
    if (notificationBell) {
        setInterval(function() {
            const url = notificationBell.dataset.url; // Data URL for fetching new notifications
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data.new_notifications > 0) {
                        notificationBell.classList.add('has-notifications');
                        notificationBell.setAttribute('data-count', data.new_notifications);
                    } else {
                        notificationBell.classList.remove('has-notifications');
                        notificationBell.removeAttribute('data-count');
                    }
                })
                .catch(error => console.error('Error fetching notifications:', error));
        }, 30000); // Fetch every 30 seconds
    }

    // Real-time validation for leave application form (date range)
    const leaveStartDate = document.querySelector('#leave-start-date');
    const leaveEndDate = document.querySelector('#leave-end-date');

    if (leaveStartDate && leaveEndDate) {
        leaveStartDate.addEventListener('change', validateLeaveDates);
        leaveEndDate.addEventListener('change', validateLeaveDates);
    }

    function validateLeaveDates() {
        const startDate = new Date(leaveStartDate.value);
        const endDate = new Date(leaveEndDate.value);

        if (endDate < startDate) {
            alert('End date cannot be earlier than start date.');
            leaveEndDate.style.borderColor = 'red';
        } else {
            leaveEndDate.style.borderColor = '#ccc';
        }
    }

    // Animations for page interactions
    const fadeInElements = document.querySelectorAll('.fade-in');
    fadeInElements.forEach(element => {
        element.style.opacity = 0;
        window.addEventListener('scroll', function() {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight;

            if (elementPosition < screenPosition) {
                element.style.transition = 'opacity 1s ease-in-out';
                element.style.opacity = 1;
            }
        });
    });
});
