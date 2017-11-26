import tensorflow as tf


treat = {'Alopecia' : 'The most commonly used drugs for alopecia prescribed that either promote hair growth or affect the immune system are Minoxidil, Anthralin, SADBE, and DPCP. Some alternative treatment methods such as acupuncture and aromatherapy are also popular, although there is little, if any, evidence to support these treatments. The use of photochemotherapy is supported by some studies and presents a potential alternative for patients unable or unwilling to use systemic or invasive therapies. For more medical assistance, kindly consult the nearest dermatologist as we have indicated in the adjacent map. May you get well soon! Thanks for using our app.',
 'Eczema' : 'Treatment for Exzema: In many cases eczema is manageable, especially with a proper skin care routine. This includes bathing and moisturizing daily, sometimes in combination with prescription medications and/or alternative therapies. Some basic things you can do to help control eczema: 1.  Establish a daily skin care routine - just like you would for other activities such as brushing your teeth. Try not to miss treatments, but be flexible if your symptoms change. 2.  Recognize stressful situations and events - and learn to avoid or cope with them by using techniques for stress management. You may do this on your own, or with the help of your doctor or psychologist. 3.  Be mindful of scratching and rubbing - and limit contact with materials or substances that may irritate your skin. 4.  Dress in soft, breathable clothing and avoid itchy fabrics like wool, that can further irritate your eczema. You can consult a dermatologist near you. This is indicated in the map. Stay hydrated and Good luck!', 'Acne' : 'The most common types of medicines that doctors use to treat acne include: 1.  Benzoyl peroxide, such as Brevoxyl or Triaz.  2.  Salicylic acid, such as Propa pH or Stridex. 3.  Topical and oral antibiotics, such as clindamycin, doxycycline, erythromycin, and tetracycline. 4.  Topical retinoid medicines, such as tretinoin (Retin-A), adapalene (Differin), and tazarotene (Tazorac). 5.  Azelaic acid, such as Azelex, a topical cream. 6.  Isotretinoin, an oral retinoid. 7.  Low-dose birth control pills that contain estrogen (such as Estrostep, Ortho Tri-Cyclen, or Yaz), which work well on moderate acne in women and for premenstrual flare-ups. 8. Androgen blockers, such as spironolactone. Androgen blockers can be useful in treating acne. These medicines decrease the amount of sebum (oil) made in your pores. What to think about If you are pregnant, talk to your doctor about whether you should take antibiotics for acne. Some antibiotics aren\'t safe to take during pregnancy. Over time, bacteria can become resistant to antibiotics, which means that the antibiotics are no longer effective at killing or controlling the bacteria causing the acne. This is called drug resistance. When this occurs, a different antibiotic may be used. You can consult a dermatologist near you. This is indicated in the map. Good Luck!', 'Normal' : 'Your skin seem to be completely fine! Chill out!'}


def test(image_path):

    RESULT = ""

    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()
    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
        in tf.gfile.GFile("diagnosis/model/retrained_lebels.txt")]
    # Unpersists graph from file
    with tf.gfile.FastGFile("diagnosis/model/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    # Feed the image_data as input to the graph and get first prediction
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, 
        {'DecodeJpeg/contents:0': image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if(score > 0.5):
                RESULT = human_string
    return (RESULT, treat[RESULT]);