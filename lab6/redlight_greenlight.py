import cv2

cap = cv2.VideoCapture(0)

_, first = cap.read()

while True:
    _, second = cap.read()

    orig = second.copy()

    diff = cv2.absdiff(second, first)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    _, contors, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contor in contors:
        if cv2.contourArea(contor) > 5000:
            (x, y, w, h) = cv2.boundingRect(contor)
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(orig, "MOTION-DETECTED", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("", orig)

    first = second.copy()

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
