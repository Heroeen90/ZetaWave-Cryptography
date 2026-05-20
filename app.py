import numpy as np
import matplotlib.pyplot as plt

# 1. تزويد النظام بأجزاء تخيلية لأول بضعة أصفار معروفة لدالة زيتا (γ)
# هذه الأرقام هي الارتفاعات الفوقية للأصفار على خط الحرج Re(s) = 0.5
RIEMANN_ZEROS = [
    14.134725142,  # الصفر الأول
    21.022039639,  # الصفر الثاني
    25.010857580,  # الصفر الثالث
    30.424876126,  # الصفر الرابع
    32.935061588,  # الصفر الخامس
    37.586178159,  # الصفر السادس
    40.918719012   # الصفر السابع
]

def riemann_wave_generator(x, zeros):
    """
    محاكاة لتوليد الموجات التراكمية بناءً على أصفار ريمان.
    كل صفر يساهم بنغمة (موجة جيبية) تعتمد على اللوغاريتم الطبيعي لـ x.
    """
    wave_sum = np.zeros_like(x, dtype=float)
    
    # دمج الترددات الموجية للأصغار
    for gamma in zeros:
        # الصيغة الرياضية المبسطة لتذبذب ريمان: sin(gamma * ln(x)) / gamma
        # قمنا بحماية الكود من القيمة صفر عبر إضافة إبسيلون صغير جداً
        wave_sum += np.sin(gamma * np.log(x + 1e-9)) / (gamma * 0.5)
        
    return wave_sum

# 2. إعداد نطاق البحث (مستقيم الأعداد من 2 إلى 30)
x_values = np.linspace(2, 30, 1000)

# 3. إطلاق الموجة الرياضية المركبة
calculated_waves = riemann_wave_generator(x_values, RIEMANN_ZEROS)

# 4. تحديد الأعداد الأولية الحقيقية في هذا النطاق للمقارنة البصرية
actual_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# 5. رسم النتيجة لرؤية التداخل البناء (Constructive Interference)
plt.figure(figsize=(12, 6))
plt.plot(x_values, calculated_waves, label='موجة ريمان التراكمية (Zeta Wave)', color='blue', lw=2)

# وضع علامات عند الأعداد الأولية الحقيقية لنرى هل تنبأت الموجة بها
for prime in actual_primes:
    plt.axvline(x=prime, color='red', linestyle='--', alpha=0.7, label='عدد أولي حقيقي' if prime == 2 else "")

plt.title("محاكاة تحويل أصفار ريمان إلى موجات للتنبؤ بالأعداد الأولية")
plt.xlabel("مستقيم الأعداد (X)")
plt.ylabel("سعة الموجة (تداخل الترددات)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
