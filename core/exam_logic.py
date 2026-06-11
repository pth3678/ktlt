from algorithms import shuffle

def generate_exam(bank, subject, difficulty, count, seed):
    """
    1. Lọc câu hỏi theo môn học và độ khó.
    2. Xáo trộn ngân hàng và lấy số lượng cần thiết.
    3. Xáo trộn đáp án của từng câu hỏi.
    """
    # Lọc câu hỏi
    filtered = [q for q in bank if q['subject'] == subject and q['difficulty'] == difficulty]
    
    if len(filtered) < count:
        return None # Hoặc raise một lỗi tùy bạn xử lý
    
    # Xáo trộn danh sách câu hỏi theo seed
    shuffled_questions = shuffle(filtered, seed)
    exam_data = shuffled_questions[:count]
    
    # Xáo trộn đáp án (A, B, C, D) cho từng câu
    for q in exam_data:
        q['answers'] = shuffle(q['answers'], seed)
        
    return exam_data

def grade_and_analyze(user_answers, exam_data, time_taken):
    """
    Chấm điểm và trả về dữ liệu chi tiết cho Dashboard.
    user_answers: list đáp án của sinh viên (ví dụ: ["A", "C", ...])
    """
    correct_count = 0
    analysis = []
    
    for i, q in enumerate(exam_data):
        # Giả sử q['correct_answer'] là giá trị đáp án đúng (ví dụ: "A")
        if user_answers[i] == q['correct_answer']:
            correct_count += 1
        else:
            analysis.append({
                "question": q['text'],
                "user_choice": user_answers[i],
                "correct": q['correct_answer']
            })
            
    # Tính điểm thang 10
    total = len(exam_data)
    score = (correct_count / total) * 10
    
    return {
        "score": round(score, 2),
        "correct_count": correct_count,
        "total": total,
        "time_taken": time_taken,
        "analysis": analysis
    }