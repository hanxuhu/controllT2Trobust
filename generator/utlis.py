import os
import subprocess
from subprocess import call

def eval_totto(prediction_path, target_path):
    command = 'bash language/totto/totto_eval.sh --prediction_path ' + prediction_path + ' --target_path ' + target_path
    try:
        result = subprocess.run(command,
            check=True,
            shell=True,
            stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    res = result.stdout.decode("utf-8") 
    res=str(res)
    #print(res)
    #res=res[0]
    #print(res)
    content_list = res.split(r'BLEU')
    #content_list = content_list.split(r'BLEU')
    #content_list[2].split(': ')[1].split(',')[0]
    #print(content_list)

    overall_bleu = float(content_list[2].split(': ')[1].split(',')[0])
    overlap_bleu = float(content_list[4].split(': ')[1].split(',')[0])
    nonoverlap_bleu = float(content_list[6].split(': ')[1].split(',')[0])
    return overall_bleu, overlap_bleu, nonoverlap_bleu

