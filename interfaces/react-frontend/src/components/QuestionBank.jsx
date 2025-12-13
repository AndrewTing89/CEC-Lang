import { useState, useEffect } from 'react'

function QuestionBank() {
  const [questions, setQuestions] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [expandedId, setExpandedId] = useState(null)
  const [searchTerm, setSearchTerm] = useState('')

  useEffect(() => {
    fetchQuestions()
  }, [])

  const fetchQuestions = async () => {
    try {
      const response = await fetch('/questions')
      if (!response.ok) throw new Error('Failed to load questions')
      const data = await response.json()
      setQuestions(data.questions)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const toggleExpand = (id) => {
    setExpandedId(expandedId === id ? null : id)
  }

  const filteredQuestions = questions.filter(q =>
    q.question.toLowerCase().includes(searchTerm.toLowerCase()) ||
    q.id.toLowerCase().includes(searchTerm.toLowerCase()) ||
    q.expected_answer.toLowerCase().includes(searchTerm.toLowerCase())
  )

  if (loading) {
    return (
      <div className="questions-loading">
        <div className="loading-spinner"></div>
        <p>Loading questions...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="questions-error">
        <p>Error loading questions: {error}</p>
        <button onClick={fetchQuestions}>Retry</button>
      </div>
    )
  }

  return (
    <div className="question-bank">
      <div className="question-bank-header">
        <h2>CEC 2022 Evaluation Questions</h2>
        <p className="question-count">{questions.length} questions total</p>
      </div>

      <div className="search-box">
        <input
          type="text"
          placeholder="Search questions..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        {searchTerm && (
          <span className="search-results">
            {filteredQuestions.length} results
          </span>
        )}
      </div>

      <div className="questions-list">
        {filteredQuestions.map((q, idx) => (
          <div
            key={q.id}
            className={`question-item ${expandedId === q.id ? 'expanded' : ''}`}
          >
            <div
              className="question-header"
              onClick={() => toggleExpand(q.id)}
            >
              <span className="question-number">Q{idx + 1}</span>
              <span className="question-id">[{q.id}]</span>
              <span className="question-text">
                {q.question.length > 100
                  ? q.question.substring(0, 100) + '...'
                  : q.question}
              </span>
              <span className="expand-icon">
                {expandedId === q.id ? '▼' : '▶'}
              </span>
            </div>

            {expandedId === q.id && (
              <div className="question-details">
                <div className="detail-section">
                  <h4>Full Question:</h4>
                  <p>{q.question}</p>
                </div>
                <div className="detail-section expected-answer">
                  <h4>Expected Answer:</h4>
                  <p>{q.expected_answer}</p>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {filteredQuestions.length === 0 && searchTerm && (
        <div className="no-results">
          <p>No questions found matching "{searchTerm}"</p>
        </div>
      )}
    </div>
  )
}

export default QuestionBank
