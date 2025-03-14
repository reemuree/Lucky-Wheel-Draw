document.addEventListener("DOMContentLoaded", function() {
    const users = JSON.parse(document.getElementById("user-data").textContent);
    
    document.getElementById("spin-btn").addEventListener("click", function() {
        if (users.length === 0) {
            alert("কোনো ইউজার এন্ট্রি নেই!");
            return;
        }

        let winnerIndex = Math.floor(Math.random() * users.length);
        let winner = users[winnerIndex];

        document.getElementById("winner-name").textContent = winner.name;
        document.getElementById("winner-phone").textContent = winner.phone;
        document.getElementById("winner-alert").style.display = "block";
    });
    document.addEventListener("DOMContentLoaded", function() {
        const users = JSON.parse(document.getElementById("user-data").textContent);
    
        document.getElementById("spin-btn").addEventListener("click", function() {
            if (users.length === 0) {
                alert("কোনো ইউজার এন্ট্রি নেই!");
                return;
            }
    
            let winnerIndex = Math.floor(Math.random() * users.length);
            let winner = users[winnerIndex];
    
            document.getElementById("winner-name").textContent = winner.name;
            document.getElementById("winner-phone").textContent = winner.phone;
            document.getElementById("winner-alert").style.display = "block";
    
            // বিজয়ীর তথ্য সার্ভারে পাঠানো
            fetch('/winner', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(winner)
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
        });
    });
    
});
