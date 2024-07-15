const quizContainer = document.getElementById('quiz');
const resultsContainer = document.getElementById('results');
const nextButton = document.getElementById('next');
const timerContainer = document.getElementById('timer');
const timeLeftSpan = document.getElementById('time-left');

const quizQuestions = [
    {
        question: "Who is known as the 'father of haute couture'?",
        answers: {
            a: "Coco Chanel",
            b: "Christian Dior",
            c: "Charles Frederick Worth"
        },
        correctAnswer: "c"
    },
    {
        question: "What year was the first New York Fashion Week held?",
        answers: {
            a: "1943",
            b: "1951",
            c: "1965"
        },
        correctAnswer: "a"
    },
    {
        question: "Which fashion house is known for its iconic 'LV' monogram?",
        answers: {
            a: "Gucci",
            b: "Louis Vuitton",
            c: "Prada"
        },
        correctAnswer: "b"
    }
];

let currentQuestionIndex = 0;
let numCorrect = 0;
let timer;

function buildQuiz() {
    const currentQuestion = quizQuestions[currentQuestionIndex];

    document.getElementById('question').textContent = currentQuestion.question;
    document.getElementById('labelA').textContent = currentQuestion.answers.a;
    document.getElementById('labelB').textContent = currentQuestion.answers.b;
    document.getElementById('labelC').textContent = currentQuestion.answers.c;

    startTimer();
}

function startTimer() {
    let timeLeft = 10;
    timeLeftSpan.textContent = timeLeft;

    timer = setInterval(() => {
        timeLeft--;
        timeLeftSpan.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(timer);
            nextQuestion();
        }
    }, 1000);
}

function nextQuestion() {
    clearInterval(timer);

    const answer = document.querySelector('input[name="answer"]:checked');
    if (answer && answer.value === quizQuestions[currentQuestionIndex].correctAnswer) {
        numCorrect++;
    }

    currentQuestionIndex++;
    if (currentQuestionIndex < quizQuestions.length) {
        buildQuiz();
    } else {
        showResults();
    }
}

function showResults() {
    quizContainer.style.display = 'none';
    timerContainer.style.display = 'none';
    nextButton.style.display = 'none';

    if (numCorrect === quizQuestions.length) {
        resultsContainer.innerHTML = `<p>Congratulations! You got all ${quizQuestions.length} questions correct!</p>`;
    } else {
        resultsContainer.innerHTML = `<p>Better luck next time! You got ${numCorrect} out of ${quizQuestions.length} correct.</p>`;
    }
}

nextButton.addEventListener('click', nextQuestion);
buildQuiz();
