import traceback

def log(f):
    log_data = {}
    log_data["name"] = f.func_name

    def new_f(*args, **kwargs):
        log_data["args"] = args
        log_data["kwargs"] = kwargs
        try:
            print "aaa:",f
            res = f(*args, **kwargs)
            log_data["res"] = res
        except Exception as e:
            log_data["error"] = e
            log_data["traceback"] = traceback.format_exc()
             
        print "log_data:", log_data

        if "res" in log_data:
            return log_data["res"]
        else:
            raise log_data["error"]            
    return new_f

    
