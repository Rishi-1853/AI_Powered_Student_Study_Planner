const ctx = document.getElementById(
    'studyChart'
);

new Chart(ctx, {

    type: 'bar',

    data: {

        labels: [

            'Math',
            'Physics',
            'Programming',
            'English',
            'Chemistry'
        ],

        datasets: [{

            label: 'Study Hours',

            data: [

                8,
                6,
                10,
                4,
                5
            ]
        }]
    }
});