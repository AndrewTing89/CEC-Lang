import { useState, useRef, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'
import VoiceRecorder from './components/VoiceRecorder'
import QuestionBank from './components/QuestionBank'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [includeNecComparison, setIncludeNecComparison] = useState(false)
  const [currentPage, setCurrentPage] = useState('assistant')
  const messagesEndRef = useRef(null)

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const handleSubmit = async (e) => {
    e?.preventDefault()
    if (!input.trim() || isLoading) return

    const userMessage = input.trim()
    setInput('')
    setMessages(prev => [...prev, { role: 'user', content: userMessage }])
    setIsLoading(true)

    try {
      const response = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: userMessage,
          include_nec_comparison: includeNecComparison
        })
      })

      if (!response.ok) throw new Error('Failed to get response')

      const data = await response.json()
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: data.answer,
        metadata: {
          model: data.model,
          duration: data.duration_seconds,
          toolCalls: data.tool_calls
        }
      }])
    } catch (error) {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: `Error: ${error.message}`,
        isError: true
      }])
    } finally {
      setIsLoading(false)
    }
  }

  const handleTranscription = (text) => {
    setInput(text)
  }

  const clearConversation = async () => {
    try {
      await fetch('/clear', { method: 'POST' })
      setMessages([])
    } catch (error) {
      console.error('Failed to clear conversation:', error)
    }
  }

  // Render page content based on current page
  const renderPageContent = () => {
    switch (currentPage) {
      case 'questions':
        return (
          <>
            <header className="main-header">
              <h1>Question Bank</h1>
            </header>
            <div className="page-content">
              <QuestionBank />
            </div>
          </>
        )
      case 'about':
        return (
          <>
            <header className="main-header">
              <h1>About CEC Agent</h1>
            </header>
            <div className="page-content about-page">
              <h2>What is CEC Agent?</h2>
              <p>
                <strong>CEC Agent</strong> is an AI-powered assistant for the California Electrical Code (CEC 2022)
                with NEC 2023 comparison support. It helps electricians, inspectors, engineers, and students get fast,
                accurate answers about California electrical code requirements with verified citations and calculations.
              </p>

              <h2>Anti-Hallucination Features</h2>
              <div className="feature-box">
                <h3>Verified Source Requirement</h3>
                <p>Every code citation must come from the actual CEC/NEC database. The AI cannot cite sections from memory.</p>
              </div>
              <div className="feature-box">
                <h3>Deterministic Table Lookups</h3>
                <p>All table values are looked up from official CEC/NEC tables stored as structured data. No guessing allowed.</p>
              </div>
              <div className="feature-box">
                <h3>Mandatory Exception Checking</h3>
                <p>Before answering, the system searches for exceptions that might apply to your specific situation.</p>
              </div>
              <div className="feature-box">
                <h3>Transparent Calculations</h3>
                <p>All math is executed step-by-step with Python code. Every calculation shows the formula and intermediate steps.</p>
              </div>

              <h2>Who is it for?</h2>
              <ul>
                <li><strong>Electricians</strong> - Get quick answers while on the job site in California</li>
                <li><strong>Electrical Inspectors</strong> - Verify CEC compliance for installations</li>
                <li><strong>Engineers</strong> - Check California requirements during design and planning</li>
                <li><strong>Students</strong> - Learn California electrical code with clear explanations</li>
                <li><strong>Contractors</strong> - Plan projects with accurate load calculations per CEC</li>
              </ul>
            </div>
          </>
        )
      default: // assistant
        return (
          <>
            <header className="main-header">
              <h1>California Electrical Code Assistant</h1>
            </header>

            {/* Chat Messages */}
            <div className="chat-container">
              {messages.length === 0 && (
                <div className="welcome-message">
                  <p>
                    <strong>CEC Agent</strong> is an AI-powered assistant for the California Electrical Code (CEC 2022)
                    with NEC 2023 comparison support. It helps electricians, inspectors, engineers, and students get fast,
                    accurate answers about California electrical code requirements with verified citations and calculations.
                  </p>
                  <p>
                    Unlike general AI tools that can give incorrect information, CEC Agent is specifically designed
                    to provide accurate, trustworthy California electrical code guidance you can rely on for professional work.
                  </p>
                </div>
              )}

              {messages.map((msg, idx) => (
                <div key={idx} className={`message ${msg.role}`}>
                  <div className="message-avatar">
                    {msg.role === 'user' ? '👤' : '⚡'}
                  </div>
                  <div className="message-content">
                    {msg.role === 'assistant' ? (
                      <ReactMarkdown>{msg.content}</ReactMarkdown>
                    ) : (
                      <p>{msg.content}</p>
                    )}
                    {msg.metadata && (
                      <div className="message-metadata">
                        <span>Model: {msg.metadata.model}</span>
                        <span>Time: {(msg.metadata.duration * 1000).toFixed(0)}ms</span>
                        <span>Tools: {msg.metadata.toolCalls?.length || 0}</span>
                      </div>
                    )}
                  </div>
                </div>
              ))}

              {isLoading && (
                <div className="message assistant">
                  <div className="message-avatar">⚡</div>
                  <div className="message-content">
                    <div className="loading-indicator">
                      <span></span><span></span><span></span>
                      Analyzing California Electrical Code...
                    </div>
                  </div>
                </div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <form className="input-area" onSubmit={handleSubmit}>
              <VoiceRecorder onTranscription={handleTranscription} />
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask about CEC 2022 or NEC 2023 electrical codes..."
                disabled={isLoading}
              />
              <button type="submit" disabled={isLoading || !input.trim()}>
                Ask
              </button>
            </form>
          </>
        )
    }
  }

  return (
    <div className="app">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="sidebar-header">
          <h1>CEC Lang</h1>
        </div>

        <nav className="sidebar-nav">
          <button
            className={`nav-button ${currentPage === 'assistant' ? 'active' : ''}`}
            onClick={() => setCurrentPage('assistant')}
          >
            Assistant
          </button>
          <button
            className={`nav-button ${currentPage === 'questions' ? 'active' : ''}`}
            onClick={() => setCurrentPage('questions')}
          >
            Questions
          </button>
          <button
            className={`nav-button ${currentPage === 'about' ? 'active' : ''}`}
            onClick={() => setCurrentPage('about')}
          >
            About
          </button>
        </nav>

        {currentPage === 'assistant' && (
          <>
            <div className="sidebar-section">
              <h3>Settings</h3>
              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={includeNecComparison}
                  onChange={(e) => setIncludeNecComparison(e.target.checked)}
                />
                Include NEC comparison
              </label>
            </div>

            <div className="sidebar-section">
              <h3>Conversation</h3>
              <button className="clear-button" onClick={clearConversation}>
                Clear Conversation
              </button>
            </div>
          </>
        )}

        <div className="sidebar-footer">
          <p><strong>Powered by:</strong></p>
          <p>CEC 2022 + NEC 2023</p>
          <p>Hybrid Search</p>
          <p>Custom Tools</p>
        </div>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        {renderPageContent()}
      </main>
    </div>
  )
}

export default App
