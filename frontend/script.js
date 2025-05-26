async function predictAdmission() {
    const gre = document.getElementById("gre").value || null;
    const toefl = document.getElementById("toefl").value || null;
    const rating = document.getElementById("rating").value || null;
    const sop = document.getElementById("sop").value || null;
    const lor = document.getElementById("lor").value || null;
    const gpa = document.getElementById("gpa").value || null;
    const research = document.getElementById("research").value || null;
    const score12 = document.getElementById("score12").value || null;
    const cgpa = document.getElementById("cgpa").value || null;

    // Create an object with form data
    const data = {
        gre: gre,
        toefl: toefl,
        rating: rating,
        sop: sop,
        lor: lor,
        gpa: gpa,
        research: research,
        score12: score12,
        cgpa: cgpa
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        document.getElementById("result").innerText = `Admission Chance: ${result.prediction}`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error predicting admission chance.";
    }
}
